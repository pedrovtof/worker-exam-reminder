class CustomerMessage():
    def __init__(self, clinic_name: str):
        self._default_message: str = "Olá, _USER_FIRST_NAME_! Lembrete da clinica _CLINIC_NAME_: amanhã (_DAY_/_MONTH_) você tem _EXAM_NAME_."
        self._message_with_fast : str = "Jejum: a partir das _HH_MM_ do dia _DAY_/_MONTH_, não coma nem beba nada além de água."
        self._message_with_x_ray: str = "Raio-x: retire brincos, colares e objetos de metal antes do exame."
        self._clinic_name:str = clinic_name
        self._message:str = None

    def get_message(self)->str:
        return self._message
