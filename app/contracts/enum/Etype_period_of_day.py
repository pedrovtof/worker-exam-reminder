from enum import Enum

class EtypePeriodOfDay(Enum):
    """
        MORNING     => 06-12
        AFTERNOON   => 12-16
        EVENING     => 16-18
        NIGHT       => 18-22 
    """
    MORNING=1
    AFTERNOON=2
    EVENING=3
    NIGHT=4