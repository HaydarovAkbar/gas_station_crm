from enum import Enum, auto


class States(Enum):
    START = auto()
    FUEL_COLUMN = auto()
    CHANGE_COLUMN = auto()
    CHANGE_COLUMN_NUM = auto()
    CHANGE_COLUMN_NUM_LAST = auto()
    FUEL_TYPE = auto()
    FUEL_TYPE_SALE = auto()
    FUEL_COLUMN_SALE_PT = auto()
    FUEL_SALE_SIZE = auto()
    FUEL_TYPE_PRICE = auto()
    FUEL_PRICE_INPUT = auto()
    FUEL_COLUMN_SALE = auto()
    KASSIR_SETTINGS = auto()
    KASSIR_SETTINGS_CHANGE = auto()
    ADMIN = auto()
    GET_USERS = auto()
    ADMIN_SETTINGS = auto()
    CHANGE_LANG = auto()
    ADD_USER = auto()
    USER_ROLE = auto()
    CHANGED_USER = auto()
    USER_CONF = auto()
    WAITING_FOR_NAME = auto()
    WAITING_FOR_EMAIL = auto()
    WAITING_FOR_PHONE = auto()
    WAITING_FOR_ADDRESS = auto()
    WAITING_FOR_CONFIRMATION = auto()
    FINISHED = auto()
    CANCELLED = auto()

    LEADER = auto()
    L_FUEL_TYPE = auto()
    L_FUEL_SIZE = auto()

    NOTSTART = auto()
    ADD_TODAY_DATA = auto()
    ADD_FUEL_COLUMN_NUM = auto()
    DATA_TYPE = auto()
    CHOOSE_PAYMENT_TYPE = auto()
    ADD_FUEL_PRICE_TODAY = auto()
