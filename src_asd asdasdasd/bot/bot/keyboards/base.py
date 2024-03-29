from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from ..static.base import Button as B
from ..static.base import KButtons as KB
from ..static.base import LeaderKeyboardText as LB

bt = B()
kb = KB()
lb = LB()


class KeyboardsAdmin:
    # ...
    @staticmethod
    def get_users(user_list):
        keyboard = []
        for user in user_list:
            keyboard.append([InlineKeyboardButton(user.get_fullname(), callback_data=f'{user.id}')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def get_menu(lang='uz'):
        bt_txt = bt.adm_menu[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_user_menu(lang='uz'):
        bt_txt = bt.adm_user_menu[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0]), KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def adm_settings(lang='uz'):
        bt_txt = bt.adm_settings[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_lang():
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton('🇺🇿 O\'zbekcha', callback_data='uz')],
            [InlineKeyboardButton('🇷🇺 Русский', callback_data='ru')],
            [InlineKeyboardButton('🇬🇧 English', callback_data='en')],
        ])
        return keyboard

    @staticmethod
    def back(lang='uz'):
        bt_txt = bt.adm_settings[lang]
        keyboard = [
            [KeyboardButton(bt_txt[1])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def roles(lang='uz'):
        bt_txt = bt.adm_roles[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0]), KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
            [KeyboardButton(bt_txt[3])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def user_list(users, lang='uz'):
        keyboard, txt = [], bt.inline_back[lang]
        for user in users:
            keyboard.append([InlineKeyboardButton(user.get_user(), callback_data=f'{user.chat_id}')])
        keyboard.append([InlineKeyboardButton(txt, callback_data='back')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def user_change(user_roles, lang='uz'):
        bt_txt = bt.adm_roles[lang]
        if "ADMIN" in user_roles and "KASSIR" in user_roles:
            keyboard = [
                [KeyboardButton(bt_txt[4]), KeyboardButton(bt_txt[0])],
                [KeyboardButton(bt_txt[2] + "- ✅"), KeyboardButton(bt_txt[1])],
                [KeyboardButton(bt_txt[3])],
            ]
        elif "KASSIR" in user_roles:
            keyboard = [
                [KeyboardButton(bt_txt[4]), KeyboardButton(bt_txt[0])],
                [KeyboardButton(bt_txt[2]), KeyboardButton(bt_txt[1] + "- ✅")],
                [KeyboardButton(bt_txt[3])],
            ]
        elif "ADMIN" in user_roles:
            keyboard = [
                [KeyboardButton(bt_txt[4]), KeyboardButton(bt_txt[0] + "- ✅")],
                [KeyboardButton(bt_txt[2]), KeyboardButton(bt_txt[1])],
                [KeyboardButton(bt_txt[3])],
            ]
        else:
            keyboard = [
                [KeyboardButton(bt_txt[4]), KeyboardButton(bt_txt[0])],
                [KeyboardButton(bt_txt[2]), KeyboardButton(bt_txt[1])],
                [KeyboardButton(bt_txt[3])],
            ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


class KeyboardsUser:
    # ...
    @staticmethod
    def get_menu(lang='uz'):
        bt_txt = kb.menu[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1]), KeyboardButton(bt_txt[2])],
            [KeyboardButton(bt_txt[3])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def fuel_columns(columns, lang='uz'):
        keyboard = []
        for column in columns:
            keyboard.append([InlineKeyboardButton(column.title, callback_data=f'{column.id}')])
        keyboard.append([InlineKeyboardButton(bt.inline_back[lang], callback_data='back')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def fuel_types(fuel_types, lang='uz'):
        keyboard = []
        for fuel_type in fuel_types:
            keyboard.append([InlineKeyboardButton(fuel_type.title, callback_data=f'{fuel_type.id}')])
        keyboard.append([InlineKeyboardButton(bt.inline_back[lang], callback_data='back')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def change_fuel_columns(lang='uz'):
        bt_txt = kb.fuel_columns[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0]), KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def back(lang='uz'):
        keyboard = [
            [KeyboardButton(bt.inline_back[lang])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_lang():
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton('🇺🇿 O\'zbekcha', callback_data='uz')],
            [InlineKeyboardButton('🇷🇺 Русский', callback_data='ru')],
            [InlineKeyboardButton('🇬🇧 English', callback_data='en')],
        ])
        return keyboard

    @staticmethod
    def k_settings(lang='uz'):
        bt_txt = kb.k_settings[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


class LeaderKeyboard:
    @staticmethod
    def get_menu(lang='uz'):
        bt_txt = lb.menu[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def fuel_types(fuel_types, lang='uz'):
        keyboard = []
        for fuel_type in fuel_types:
            keyboard.append([InlineKeyboardButton(fuel_type.title, callback_data=f'{fuel_type.id}')])
        keyboard.append([InlineKeyboardButton(bt.inline_back[lang], callback_data='back')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def back(lang='uz'):
        keyboard = [
            [KeyboardButton(bt.inline_back[lang])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
