from abc import ABC

class Iexam(ABC):
    def __init__(self):
        """
        Default constructor
        """
        self.id: str
        self.name: str
        self.need_preparation: bool
        self.need_xray:bool = False
        self.preparation: str

