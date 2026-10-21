from contracts.interface.Iexam import Iexam

class Rx(Iexam):
    """
    Exam for Raio-x
    """
    def __init__(self):
        super().__init__()
        self.id = "RX"
        self.name="Raio-x de tórax"
        self.need_preparation = True
        self.need_xray = True
        self.preparation = "Retirar brincos, colares e objetos metalicos"