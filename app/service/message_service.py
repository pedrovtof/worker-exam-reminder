from schemas.exam import(
    col,
    eco,
    gli,
    hem,
    rx,
    usg
)

from schemas.customer.customer_message import CustomerMessage

class MessageService(CustomerMessage):
    def __init__(self, clinic_name):
        super().__init__(clinic_name)

    def _setup_default_message(self, customer_name:str, date:str, exam_name:str):
            self._default_message = self._default_message.replace("_USER_FIRST_NAME_",customer_name)
            self._default_message = self._default_message.replace("_DAY_/_MONTH_",date)
            self._default_message = self._default_message.replace("_EXAM_NAME_",exam_name)
            self._default_message = self._default_message.replace("_CLINIC_NAME_", self._clinic_name)
            return

    def _setup_message_with_x_ray(self):
        """
            Does not need to impllement now
        """
        return

    def _setup_message_with_fast(self, hour:str, date:str):
        self._message_with_fast = self._message_with_fast.replace("_HH_MM_",hour)
        self._message_with_fast = self._message_with_fast.replace("_DAY_/_MONTH_",date)
        return

    def set_message(self, customer_name:str,exam_id:str,hour:str,date:str) -> str:
        """
        Main method to create the message to the customer
        """
        exam_identificator = exam_id.lower()
        exam = None

        match exam_identificator:
            case "col":
                exam = col.Col()
            case "eco":
                exam = eco.Eco()
            case "gli":
                exam = gli.Gli()
            case "hem":
                exam = hem.Hem()
            case "rx":
                exam = rx.Rx()
            case "usg":
                exam = usg.Usg()
            case _:
                raise ValueError(f"The exam {exam_id} is not impemented yet")

        self._setup_default_message(customer_name, date, exam.name)

        self._message = self._default_message

        if exam.need_preparation and exam.need_xray == False:
            self._setup_message_with_fast(hour,date)
            self._message += ("\n"+self._message_with_fast)

        if exam.need_preparation and exam.need_xray == True:
            self._setup_message_with_x_ray()
            self._message += ("\n"+self._message_with_x_ray)
        
        
        return self._message
