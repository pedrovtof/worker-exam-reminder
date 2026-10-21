from operator import attrgetter

from core.settings import Settings
from service.file_service import FileService
from service.message_service import MessageService
from schemas.customer.customer_scheduler import CustomerScheduler
from contracts.enum.Etype_export import EtypeExport
from contracts.enum.Etype_period_of_day import EtypePeriodOfDay
from contracts.enum.Etype_split_pattern import EtypeSplitPattern

import datetime
import pandas as pd
import time

class Worker:
    """
    Main script for process the files
    """
    def __init__(self):
        self.settings = Settings()
        self.file_service = FileService()

    async def run(self):
        """
        Start the service
        """
        print(f"begin the process of app {self.settings.app_name} in version {self.settings.app_version} with the limit in {self.settings.process_batch_limit}")
        
        today = datetime.date.today()
        tommorow = today + datetime.timedelta(days=2)
        print(f"Today is ",today)

        while True:
            
            has_itens, csv_files = await self.file_service.csv_to_be_processed(self.settings.file_path, self.settings.process_batch_limit)

            print("Files: ",len(csv_files), " is necessary continue?",has_itens)
            
            print(f"Number of files to be processed {len(csv_files)}")

            if has_itens == False:
                break

            for item in csv_files:
                
                print(f"processing => {item}")

                try:
                    df = await self.file_service.generate_dataframe_from_csv(f"{self.settings.file_path}{item}", EtypeSplitPattern(self.settings.type_split_pattern))
                    df = await self.file_service.filter_valid_customer(df,today,tommorow,"data")
                    df = await self.file_service.order_dataframe_by_hour_and_name(df, asc=True)

                    print("Customer to be processed =>\n",df)

                    customer_list : list[CustomerScheduler] = []

                    for customer in df.to_dict("records"):
                        customer_list.append(
                            CustomerScheduler(
                                customer["id"],
                                customer["paciente"],
                                customer["telefone"],
                                customer["aceita_whatsapp"],
                                customer["data"],
                                customer["hora"],
                                customer["exame"],
                                customer["situacao"]
                            )
                        )
                    
                    df= None # help to clear the memory 

                    hash_map_customer_exam = {}
                    list_of_messages = []

                    for customer in customer_list:
                        key = customer.id

                        if key not in hash_map_customer_exam:
                            hash_map_customer_exam[key] = []

                        hash_map_customer_exam[key].append(customer.exam)
                        
                    for key in hash_map_customer_exam:
                        for customer in customer_list:
                            if customer.id == key:
                                
                                message_service = MessageService(self.settings.clinic_name)
                                await customer.setup_class()

                                if await customer.validate_phone():
                                    message_service.set_message(
                                        customer_name=customer.customer,
                                        exam_id=customer.exam,
                                        hour= customer.hour,  
                                        date=customer.date.strftime("%d/%m")
                                    )
                                    print(message_service.get_message(),"\n")

                except Exception as e:
                    print(f"file to process {item} receive a exception \n{e}")

            time.sleep(2)

            #TODO: move file to a new path
            #TODO: fix message generate group by paciente in exam.