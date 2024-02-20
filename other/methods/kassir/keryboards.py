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
