from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from ..static.base import KTexts as T
from ..keyboards.base import KeyboardsUser as K
from ..states import States as S

from datetime import datetime

from bot.models import User, UserTypes, FuelColumn, FuelColumnPointer, Fuel, FuelType


def start(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        user, _ = User.objects.get_or_create(chat_id=tg_user.id, state_id=2)
        user.username = tg_user.username
        user.fullname = tg_user.full_name
        user.save()
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language
        update.message.reply_html(T().start[user_lang].format(user.fullname), reply_markup=K().get_menu(user_lang))
        return S.START


def k_fuel_type(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        fuel_types = FuelType.objects.filter(state__id=1)
        update.message.reply_text('👇👇', reply_markup=ReplyKeyboardRemove())
        update.message.reply_html(T().fuel_type[user_lang], reply_markup=K().fuel_types(fuel_types, user_lang))
        return S.FUEL_TYPE


def k_get_fuel_type(update: Update, context: CallbackContext):
    tg_user = update.callback_query.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    query = update.callback_query
    if query.data == 'back':
        query.message.delete()
        context.bot.send_message(chat_id=tg_user.id, text=T().start[user_lang].format(user.fullname),
                                 reply_markup=K().get_menu(user_lang))
        return S.START
    else:
        fuel_type = FuelType.objects.get(id=query.data)
        context.chat_data['fuel_type'] = fuel_type
        query.message.delete()

        user_organs = user.organization.all()
        fuel_columns = FuelColumn.objects.filter(state__id=1).filter(organ__in=user_organs)
        context.bot.send_message(chat_id=tg_user.id, text= T().fuel_column[user_lang], parse_mode="HTML", reply_markup=K().fuel_columns(fuel_columns, user_lang))
        return S.FUEL_COLUMN


def k_fuel_column(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_organs = user.organization.all()
        fuel_columns = FuelColumn.objects.filter(state__id=1).filter(organ__in=user_organs)
        update.message.reply_text('👇👇', reply_markup=ReplyKeyboardRemove())
        update.message.reply_html(T().fuel_column[user_lang], reply_markup=K().fuel_columns(fuel_columns, user_lang))
        return S.FUEL_COLUMN


def k_choose_column(update: Update, context: CallbackContext):
    tg_user = update.callback_query.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    query = update.callback_query
    if query.data == 'back':
        query.message.delete()
        context.bot.send_message(chat_id=tg_user.id, text=T().start[user_lang].format(user.fullname),
                                 reply_markup=K().get_menu(user_lang))
        return S.START
    else:
        column = FuelColumn.objects.get(id=query.data)
        context.chat_data['column'] = column
        query.message.delete()
        fuel_type = context.chat_data['fuel_type']
        context.bot.send_message(chat_id=tg_user.id, text=T().column_chosen[user_lang].format(fuel_type.title, column.title),
                                 parse_mode="HTML",
                                 reply_markup=K().change_fuel_columns(user_lang))
        return S.CHANGE_COLUMN


def k_change_column_first(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_html(T().fuel_column_numbers[user_lang], reply_markup=K().back(user_lang))
        return S.CHANGE_COLUMN_NUM


def k_input_column_num(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        column_num = update.message.text
        if column_num.isdigit():
            fuel_column = FuelColumn.objects.get(id=context.chat_data['column'])
            fuel_type = context.chat_data['fuel_type']
            today_fuel = Fuel.objects.filter(created__date=datetime.now().date())

        update.message.reply_html(T().column_num_error[user_lang], reply_markup=K().back(user_lang))
        return S.CHANGE_COLUMN_NUM
