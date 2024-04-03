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
    SELL_FUEL_SIZE = auto()
    SUCCES = auto()
    NAXT_DATA = auto()
    CHOOSE_FUEL_COLUMN = auto()
    PLASTIG_DATA = auto()
    ADD_TODAY_FUEL_COLUMN = auto()

    ADD_ORGANIZATION = auto()
    ADD_ORGANIZATION_PHONE = auto()
    ADD_ORGANIZATION_ADDRESS = auto()
    ADD_ORGANIZATION_LEADER = auto()
    ORGANIZATION_FUEL_TYPE = auto()
    ORGANIZATION_FUEL_COLUMN = auto()
    DELETE_ORGANIZATION = auto()
    CHOOSE_ORGANIZATION = auto()
    DELETE_USER = auto()

    MAIN_MENU_ADMIN = auto()
    GET_REPORT = auto()
    GET_REPORT_WEEK = auto()
    GET_REPORT_MONTH = auto()

    ADD_FUEL = auto()
    ADD_FUEL_TYPE = auto()
    ADD_FUEL_PRICE = auto()
    CHANGE_FUEL_PRICE = auto()
    FUEL_PRICE_INPUT = auto()

    GET_REPORT_FUEL_TYPE = auto()