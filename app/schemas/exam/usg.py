from contracts.interface.Iexam import Iexam

class Usg(Iexam):
    """
    Exam for Ultrassom
    """
    def __init__(self):
        super().__init__()
        self.id = "USG"
        self.name="Ultrassom de abdome total"
        self.need_preparation = True
        self.preparation = "Jejum de 12 horas"