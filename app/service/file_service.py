import pandas as pd
import os
import datetime
from contracts.enum.Etype_split_pattern import EtypeSplitPattern

class FileService:

    def __init__(self):
        """
        Default constructor
        """

    async def csv_to_be_processed(self, filepath:str, limit:int = 50) -> (bool | str | int):
        """
            Read all the path dir for valid files and add to the process list
            filepath => path to the file
            limit => max numbers of itens
        """
        list_files : list[str] = []

        with os.scandir(filepath) as files:
            for item in files:
                if item.is_file() and ".csv" in item.name:
                        list_files.append(item.name)

                if(len(list_files) >= limit):
                    return True, list_files

        return len(list_files) > 0, list_files

    async def filter_dataframe_from_time_range(self, dataframe: dict[any], start:datetime, end:datetime, colum_name:str)-> pd.DataFrame: 
        """
            Filter the data frame using date colum
            dataframe => pandas dataframe
            start => Y-M-D the start period
            end => Y-M-D the end period
            colum_name => name of the column (data)
        """
        return  dataframe.where( 
            (dataframe[colum_name] > start.strftime("%Y-%m-%d")) 
                & 
            (dataframe[colum_name] < end.strftime("%Y-%m-%d"))
        ).dropna()

    async def generate_dataframe_from_csv(self,filepath:str, type_split_pattern:EtypeSplitPattern) -> pd.DataFrame:
        """
            Read the csv and generate a dataframe
            filepath => filepath
            type_split_pattern=> tipe of delimiter (EtypeSplitPattern) in the csv 
        """
        print(f"File to be explore : {filepath}")

        csv_delimiter = ""

        if type_split_pattern == EtypeSplitPattern.COMMA:
            csv_delimiter = ","
        elif type_split_pattern == EtypeSplitPattern.SEMICOLON:
            csv_delimiter = ";"
        elif type_split_pattern ==EtypeSplitPattern.PIPE:
                csv_delimiter = "|"
        else:
            raise Exception(f"The value of split pattern must be valid {type_split_pattern}")

        print(f"Type of delimiter {csv_delimiter}")
        
        dataframe = pd.read_csv(
            filepath, 
            delimiter=csv_delimiter, 
            dtype={
                    "id": int, 
                    "paciente":str, 
                    "telefone":str, 
                    "aceita_whatsapp":str, 
                    "data": str,
                    "hora":str, 
                    "exame":str, 
                    "situacao":str
                },
            date_format={"data": "%d/%m/%Y"},
            parse_dates=["data"]
        )
        
        return dataframe