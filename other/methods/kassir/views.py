from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove

from .texts import MessageTexts as msg_txt
from .keryboards import KassirKeyboards as kb

from db.models import User, FuelColumnPointer, Fuel, FuelColumn, FuelType, PaymentType
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
    # fuel_column = FuelColumn.objects.filter(is_active=True)
    # context.bot.send_message(chat_id=user.chat_id,
    #                          text=msg_txt.add_fuel_column[user.language],
    #                          reply_markup=kb.fuel_columns(fuel_column, user.language))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=msg_txt.data_types.get(user.language),
                             reply_markup=kb.data_types(user.language))
    return st.DATA_TYPE


def get_data_type_first(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    update.message.reply_text('-_-',
                              reply_markup=kb.back_to_menu(user.language))
    payment_types = PaymentType.objects.filter(is_active=True)
    update.message.reply_text(msg_txt.choose_payment_type.get(user.language),
                              reply_markup=kb.fuel_columns(payment_types, user.language))
    return st.CHOOSE_PAYMENT_TYPE


def get_payment_type(update: Update, context: CallbackContext):
    query = update.callback_query
    context.chat_data['payment_type'] = query.data
    query.delete_message()
    user = User.objects.get(chat_id=update.effective_user.id)
    context.bot.send_message(chat_id=update.effective_user.id,
                             text=msg_txt.fuel_price_today.get(user.language))
    return st.ADD_FUEL_PRICE_TODAY


def get_fuel_price_today(update: Update, context: CallbackContext):
    price = update.message.text
    user = User.objects.get(chat_id=update.effective_user.id)
    if price.isdigit() and int(price) > 0:
        context.chat_data['price'] = int(price)
        update.message.reply_text(
            msg_txt.sell_fuel_size_today.get(user.language)
        )
        return st.SELL_FUEL_SIZE
    else:
        update.message.reply_text(
            text=msg_txt.fuel_price_today.get(user.language))
    return st.ADD_FUEL_PRICE_TODAY


def get_sell_fuel_size(update: Update, context: CallbackContext):
    size = update.message.text
    user = User.objects.get(chat_id=update.effective_user.id)
    if size.isdigit() and int(size) > 0:
        context.chat_data['size'] = int(size)
        update.message.reply_text(
            msg_txt.sell_fuel_size_today.get(user.language)
        )
        return st.SUCCES
    else:
        update.message.reply_text(
            text=msg_txt.fuel_price_today.get(user.language))
    return st.SELL_FUEL_SIZE


def


def get_data_type_last(update: Update, context: CallbackContext):
    print("as")


def get_fuel_column_numbers_first(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    user.fuel_column_numbers = update.message.text
    user.save()
    update.message.reply_html(text=msg_txt.add_fuel_columns.format(user.fullname),
                              reply_markup=kb.back(user.language))
    return st.ADD_FUEL_COLUMN_NUM
