from telegram import Update
from telegram.ext import CallbackContext
from .texts import KeyboardsTexts as msg_txt
from .keyboards import KeyboardBase as kb

from states import States as st
from db.models import User, OrganizationFuelTypes, FuelType, SaleFuel, FuelStorage, FuelPrice


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


def add_fuel(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        update.message.reply_html("<code>Sotib olingan yoqilg'i hajmini kiriting:</code>",
                                  reply_markup=kb.back(user.language))
        return st.ADD_FUEL


def add_fuel_size(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    fuel_size = update.message.text
    if fuel_size.isdigit() and user.exists() and int(fuel_size) > 0:
        user = user.first()
        context.user_data['fuel_size'] = fuel_size
        organ_fuel_types = OrganizationFuelTypes.objects.filter(organization=user.organization)
        update.message.reply_html("<code>Sotib olingan yoqilg'i turini tanlang:</code>",
                                  reply_markup=kb.fuel_types(organ_fuel_types))
        return st.ADD_FUEL_TYPE


def add_fuel_type(update: Update, context: CallbackContext):
    query = update.callback_query
    user = User.objects.filter(chat_id=query.from_user.id, is_active=True, is_leader=True)
    fuel_type = FuelType.objects.filter(id=query.data)
    if user.exists() and fuel_type.exists():
        user = user.first()
        fuel_type = fuel_type.first()
        context.user_data['fuel_type'] = fuel_type
        query.delete_message()
        context.bot.send_message(
            chat_id=query.from_user.id,
            text="Yoqilg'i narxini kiriting:",
            reply_markup=kb.back(user.language)
        )
        return st.ADD_FUEL_PRICE


def add_fuel_price(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    fuel_price = update.message.text
    if fuel_price.isdigit() and user.exists() and int(fuel_price) > 0:
        user = user.first()
        fuel_type = context.user_data['fuel_type']
        fuel_size = context.user_data['fuel_size']
        FuelStorage.objects.create(
            remainder=int(fuel_size),
            fuel_type=fuel_type,
            price=int(fuel_price),
            organization=user.organization,
            residual=int(fuel_size)
        )
        update.message.reply_html("Yoqilg'i muvaffaqiyatli qo'shildi!", reply_markup=kb.get_main_menu(user.language))
        return st.MAIN_MENU_ADMIN


def change_fuel_price(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    if user.exists():
        user = user.first()
        organ_fuel_types = OrganizationFuelTypes.objects.filter(organization=user.organization)
        update.message.reply_html("<code>Narxni o'zgartirish uchun yoqilg'i turini tanlang</code>",
                                  reply_markup=kb.fuel_types(organ_fuel_types))
        return st.CHANGE_FUEL_PRICE


def choose_fuel_price(update: Update, context: CallbackContext):
    query = update.callback_query
    user = User.objects.filter(chat_id=query.from_user.id, is_active=True, is_leader=True)
    fuel_type = FuelType.objects.filter(id=query.data)
    if user.exists() and fuel_type.exists():
        user = user.first()
        fuel_type = fuel_type.first()
        context.user_data['fuel_type'] = fuel_type
        query.delete_message()
        context.bot.send_message(
            chat_id=query.from_user.id,
            text="Yangi narxni kiriting:",
            reply_markup=kb.back(user.language)
        )
        return st.FUEL_PRICE_INPUT


def fuel_price_input(update: Update, context: CallbackContext):
    user = User.objects.filter(chat_id=update.effective_user.id, is_active=True, is_leader=True)
    fuel_price = update.message.text
    if fuel_price.isdigit() and user.exists() and int(fuel_price) > 0:
        user = user.first()
        fuel_type = context.user_data['fuel_type']
        FuelPrice.objects.create(
            fuel_type=fuel_type,
            price=int(fuel_price),
            organization=user.organization
        )
        update.message.reply_html("Narx muvaffaqiyatli o'zgartirildi!", reply_markup=kb.get_main_menu(user.language))
        return st.MAIN_MENU_ADMIN
