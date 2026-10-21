from contracts.interface.Iexam import Iexam

class Col(Iexam):
    """
    Exam for Colesterol
    """
    def __init__(self):
        super().__init__()
        self.id = "COL"
        self.name="Colesterol total e frações"
        self.need_preparation = True
        self.preparation = "Jejum de 12 horas"
