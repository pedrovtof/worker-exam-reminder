from contracts.interface.Iexam import Iexam

class Eco(Iexam):
    """
    Exam for Ecocardiograma
    """
    def __init__(self):
        super().__init__()
        self.id = "ECO"
        self.name="Ecocardiograma total e frações"
        self.need_preparation = False
        self.preparation = "Sem preparo"
