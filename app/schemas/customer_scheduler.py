from datetime import datetime

class CustomerScheduler:
    """
    the csv customer entity
    """

    async def __init__(self, id:str, paciente:str, telefone:str, aceita_whatsapp:str, data:str, hora:str, exame:str, situacao:str):
        """
        Main constructor
        """
        self.id : int = int(id)
        self.customer : str = paciente
        self.phone : str = await self._fix_phone(telefone)
        self.accept_whatsapp : bool = await self._fix_accept_whatsapp(aceita_whatsapp)
        self.date : datetime = await self._transform_date_to_datetime(data)
        self.hour : str
        self.exame : str
        self.situation : str

    async def _transform_date_to_datetime(self, date:str):
        """
            Transform date to datetime
        """
        return datetime.strptime(date,"%d-%m-%Y")

    async def _fix_phone(self,telefone:str) -> str:
        """
        Fix telefone value from csv
        """
        return telefone.replace("(","").replace(")","").replace("-","").replace("+","").strip()

    async def _fix_accept_whatsapp(self,aceita_whatsapp:str) -> bool:
        """
        Fix the aceita_whatsapp csv value
        """
        return aceita_whatsapp.lower() == "sim"

    def validate_phone(self)->bool:
        """
            validate if the phone is valid
        """
        return len(self.phone) in (10,11)
      
        