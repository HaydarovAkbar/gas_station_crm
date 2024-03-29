from .texts import KeyboardsTexts as msg_txt
from telegram import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup


class KeyboardBase:
    def __init__(self, *args, **kwargs):
        self._buttons = []
        self._keyboard = []

    def add(self, *args):
        self._buttons.extend(args)

    def row(self, *args):
        self._keyboard.append(args)

    def render(self):
        return self._keyboard

    def __str__(self):
        return str(self._keyboard)

    def __repr__(self):
        return str(self._keyboard)

    @staticmethod
    def get_main_menu(lang='uz'):
        txt = msg_txt.main.get(lang)
        kb = ReplyKeyboardMarkup(
            [
                [KeyboardButton(txt[0]), KeyboardButton(txt[1])],
                [KeyboardButton(txt[2]), KeyboardButton(txt[3])],
            ],
            resize_keyboard=True
        )
        return kb

    @staticmethod
    def get_report_menu(lang='uz'):
        txt = msg_txt.report.get(lang)
        kb = ReplyKeyboardMarkup(
            [
                [KeyboardButton(txt[0]), KeyboardButton(txt[1])],
                [KeyboardButton(txt[2])],
            ],
            resize_keyboard=True
        )
        return kb