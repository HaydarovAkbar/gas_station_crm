from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from .texts import KeyboardsTexts as txt


class KassirKeyboards:
    @staticmethod
    def back(lang='uz'):
        text = txt.back[lang]
        keyboard = [
            [KeyboardButton(text)],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def start(lang='uz'):
        text = txt.start[lang]
        keyboard = [
            [KeyboardButton(text)],
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def fuel_types(fuel_types, lang='uz'):
        keyboard = []
        for fuel_type in fuel_types:
            keyboard.append([InlineKeyboardButton(fuel_type.title, callback_data=f'{fuel_type.id}')])
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def fuel_columns(columns, lang='uz'):
        keyboard = []
        for column in columns:
            keyboard.append([InlineKeyboardButton(column.title, callback_data=f'{column.id}')])
        keyboard.append([InlineKeyboardButton(txt.back[lang], callback_data='back')])
        return InlineKeyboardMarkup(keyboard)
