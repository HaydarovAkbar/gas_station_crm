from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from ..dictionary import AdminButton as bt


class AdminKeyboards:
    @staticmethod
    def base():
        msg = bt.base
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [msg[0], msg[1]],
                [msg[2], msg[3]],
                [msg[4]],
            ],
            resize_keyboard=True
        )
        return keyboard

    @staticmethod
    def back():
        msg = bt.back
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [msg[0]],
            ],
            resize_keyboard=True
        )
        return keyboard

    @staticmethod
    def message():
        msg = bt.message
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [msg[0]],
                [msg[1]],
                [msg[2]],
                [msg[3]],
            ],
            resize_keyboard=True
        )
        return keyboard


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
            [KeyboardButton(bt_txt[1]), KeyboardButton(bt_txt[2])],
            [KeyboardButton(bt_txt[3])],
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

    @staticmethod
    def organization_list(org_list, lang='uz'):
        keyboard, txt = [], bt.inline_back[lang]
        for org in org_list:
            keyboard.append([InlineKeyboardButton(org.title, callback_data=f'{org.id}')])
        keyboard.append([InlineKeyboardButton(txt, callback_data='back')])
        return InlineKeyboardMarkup(keyboard)
