from contracts.interface.Iexam import Iexam

class Gli(Iexam):
    """
    Exam for GLICEMIA
    """
    def __init__(self):
        super().__init__()
        self.id = "GLI"
        self.name="Glicemia de jejum"
        self.need_preparation = True
        self.preparation = "Jejum de 8 horas"