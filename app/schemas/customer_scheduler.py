from datetime import datetime
import numpy as np
import string

class CustomerScheduler:
    """
    the csv customer entity
    """

    def __init__(self, id:str, paciente:str, telefone:str, aceita_whatsapp:str, data:str, hora:str, exame:str, situacao:str):
        """
        Main constructor
        """
        self.id : float = id
        self.customer : str = paciente
        self.phone : str = telefone
        self.accept_whatsapp : str = aceita_whatsapp
        self.date : str = data
        self.hour : str = hora
        self.exame : str = exame
        self.situation : str = situacao

    async def setup_class(self):
        self.phone = await self._fix_phone(self.phone)
        self.accept_whatsapp : bool = await self._fix_accept_whatsapp(self.accept_whatsapp)

    async def transform_date_to_datetime(self, date:datetime):
        """
            Transform date:str to datetime
        """
        return datetime.strptime(str(date),'%Y-%m-%d')

    async def _fix_phone(self,telefone:str) -> str:
        """
        Fix telefone value from csv
        """
        telefone = telefone.str.replace("(","")
        telefone = telefone.str.replace(")","")
        telefone = telefone.str.replace("-","")
        telefone = telefone.str.replace("+","")
        telefone = telefone.str.replace(" ","")
        telefone = telefone.str.strip()
        return telefone

    async def _fix_accept_whatsapp(self,aceita_whatsapp:str) -> bool:
        """
        Fix the aceita_whatsapp csv value
        """
        return aceita_whatsapp.str.lower() == "sim"

    def validate_phone(self)->bool:
        """
            validate if the phone is valid
        """
        return len(self.phone) in (10,11)
      
        