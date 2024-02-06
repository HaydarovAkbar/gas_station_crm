from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from ..static.base import Buttom as B

bt = B()

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
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_user_menu(lang='uz'):
        bt_txt = bt.adm_user_menu[lang]
        keyboard = [
            [KeyboardButton(bt_txt[0])],
            [KeyboardButton(bt_txt[1])],
            [KeyboardButton(bt_txt[2])],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)