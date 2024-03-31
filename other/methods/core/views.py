import time

from telegram import Update
from telegram.ext import CallbackContext

from decouple import config

from .texts import KeyboardsTexts as msg_txt
from .keyboards import KeyboardBase as kb

from states import States as st
from db.models import User

CHANNEL_ID = config('CHANNEL_ID')


def leader(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        update.message.reply_html(
            f"Salom, {user.fullname}!\n"
            f"Quyidagi tugmalardan birini tanlang:",
            reply_markup=kb.get_main_menu()
        )
        return st.MAIN_MENU_ADMIN


def get_report(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        update.message.reply_html("Hisobot turini tanlang!", reply_markup=kb.get_report_menu(user.language))
        return st.GET_REPORT


def get_report_week(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        update.message.reply_html("Haftalik hisobot turi!", reply_markup=kb.get_report_menu(user.language))
        return st.GET_REPORT_WEEK


def get_report_month(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        update.message.reply_html("Oylik hisobot turi!", reply_markup=kb.get_report_menu(user.language))
        return st.GET_REPORT_MONTH