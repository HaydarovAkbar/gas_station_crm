from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove

from .texts import MessageTexts as msg_txt
from .keryboards import KassirKeyboards as kb

from db.models import User, FuelColumnPointer, Fuel, FuelColumn, FuelType
from states import States as st


def send_night_notification(context: CallbackContext):
    users = User.objects.filter(is_active=True)  # , position__icontains='KASSIR'
    for user in users:
        context.bot.send_message(
            chat_id=user.chat_id,
            text=msg_txt.start_notification[user.language],
            reply_markup=kb.start(user.language)
        )
    return st.NOTSTART


def get_start(update: Update, context: CallbackContext):
    user, _ = User.objects.get_or_create(chat_id=update.effective_user.id,
                                         defaults={'username': update.effective_user.username,
                                                   'fullname': update.effective_user.full_name
                                                   })
    if user and user.is_active:
        update.message.reply_html(msg_txt.lets_start[user.language], reply_markup=ReplyKeyboardRemove())
        fuel_type = FuelType.objects.filter(is_active=True)
        update.message.reply_html(text=msg_txt.add_fuel_type[user.language].format(user.fullname),
                                  reply_markup=kb.fuel_types(fuel_type, user.language))
        return st.ADD_TODAY_DATA


def get_fuel_type(update: Update, context: CallbackContext):
    query = update.callback_query
    fuel_type = FuelType.objects.get(id=update.callback_query.data)
    context.user_data['fuel_type'] = fuel_type
    query.delete_message()
    user = User.objects.get(chat_id=update.effective_chat.id)
    fuel_column = FuelColumn.objects.filter(is_active=True)
    context.bot.send_message(chat_id=user.chat_id,
                             text=msg_txt.add_fuel_column[user.language],
                             reply_markup=kb.fuel_columns(fuel_column, user.language))
    return st.ADD_FUEL_COLUMN_NUM


def get_fuel_column_numbers_first(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    user.fuel_column_numbers = update.message.text
    user.save()
    update.message.reply_html(text=msg_txt.add_fuel_columns.format(user.fullname),
                              reply_markup=kb.back(user.language))
    return st.ADD_FUEL_COLUMN_NUM
