from contracts.interface.Iexam import Iexam

class Hem(Iexam):
    """
    Exam for Hemograma
    """
    def __init__(self):
        super().__init__()
        self.id = "HEM"
        self.name="Hemograma completo"
        self.need_preparation = False
        self.preparation = "Sem preparo"