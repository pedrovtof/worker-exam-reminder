from core.settings import Settings
from service.file_service import FileService
from contracts.enum.Etype_export import EtypeExport
from contracts.enum.Etype_period_of_day import EtypePeriodOfDay
from contracts.enum.Etype_split_pattern import EtypeSplitPattern
import datetime

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


        while True:
            
            has_itens, csv_files = await self.file_service.csv_to_be_processed(self.settings.file_path, self.settings.process_batch_limit)
            
            print(f"Number of files {len(csv_files)}")

            if has_itens == False:
                break

            for item in csv_files:
                
                print(f"file to process => {item}")

                try:
                    df = await self.file_service.generate_dataframe_from_csv(f"{self.settings.file_path}{item}", EtypeSplitPattern(self.settings.type_split_pattern))

                    param_1 = df["data"] > today.strftime("%Y-%m-%d")
                    param_2 = df["data"] < tommorow.strftime("%Y-%m-%d")

                    print(
                        df.where(param_1 and param_2)
                          ) 

                except Exception as e:
                    print(f"file to process {item} receive a exception \n{e}")

                break # REMOVER

            break # REMOVER
            
            time.sleep(1)