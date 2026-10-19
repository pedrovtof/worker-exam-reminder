from enum import Enum

class EtypeSplitPattern(Enum):
    """
        COMMA => ,
        SEMICOLON => ;
        PIPE => |
    """
    COMMA=1
    SEMICOLON=2
    PIPE=3