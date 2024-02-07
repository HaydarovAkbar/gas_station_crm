from enum import Enum, auto


class States(Enum):
    START = auto()
    ADMIN = auto()
    GET_USERS = auto()
    ADMIN_SETTINGS = auto()
    CHANGE_LANG = auto()
    LEADER = auto()
    WAITING_FOR_NAME = auto()
    WAITING_FOR_EMAIL = auto()
    WAITING_FOR_PHONE = auto()
    WAITING_FOR_ADDRESS = auto()
    WAITING_FOR_CONFIRMATION = auto()
    FINISHED = auto()
    CANCELLED = auto()
