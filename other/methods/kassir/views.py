from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove

from .texts import MessageTexts as msg_txt
from .keryboards import KassirKeyboards as kb

from db.models import User, FuelColumnPointer, Fuel, FuelColumn, FuelType, PaymentType, OrganizationFuelTypes, SaleFuel, \
    OrganizationFuelColumns, FuelColumnPointer
from states import States as st
from django.utils import timezone


def send_night_notification(context: CallbackContext):
    users = User.objects.filter(is_active=True, is_cashier=True)
    for user in users:
        try:
            context.bot.send_message(
                chat_id=user.chat_id,
                text=msg_txt.start_notification[user.language],
                reply_markup=kb.start(user.language)
            )
        except Exception:
            pass
    return st.NOTSTART


def get_start(update: Update, context: CallbackContext):
    user, _ = User.objects.get_or_create(chat_id=update.effective_user.id,
                                         defaults={'username': update.effective_user.username,
                                                   'fullname': update.effective_user.full_name
                                                   })
    if user and user.is_active:
        update.message.reply_html(msg_txt.lets_start[user.language], reply_markup=ReplyKeyboardRemove())
        organization_fuel_types = OrganizationFuelTypes.objects.filter(organization=user.organization)
        msg, i = "", 0
        for org_fuel_type in organization_fuel_types:
            fuel_data = SaleFuel.objects.filter(fuel_type=org_fuel_type.fuel_type,
                                                created_at__date=timezone.now().date())
            if fuel_data:
                i += 1
                msg += f"{org_fuel_type.fuel_type.title} - ✅\n"
            else:
                msg += f"{org_fuel_type.fuel_type.title} ❗️\n"
        if i == organization_fuel_types.count():
            return fuel_column_pointer(update, context)
        user_fuel_type_txt = f"""
<b>{user.fullname}</b> - <code>{user.organization.title}</code> tashkiloti uchun:

<i>Bugungi hisobotlarni kiriting</i>

{msg}

Yuqoridagi yoqilg'ilar uchun ma'lumotlar kiritish uchun pastdagi tugmalardan birini tanlang 👇
"""
        update.message.reply_html(text=user_fuel_type_txt,
                                  reply_markup=kb.organ_fuel_types(organization_fuel_types, user.language))
        return st.ADD_TODAY_DATA


def get_fuel_type(update: Update, context: CallbackContext):
    query = update.callback_query
    fuel_type = FuelType.objects.get(id=update.callback_query.data)
    context.user_data['fuel_type'] = fuel_type
    query.delete_message()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<code>Bugungi naxt holatdagi savdo hajmini kiriting</code> [litr]",
                             parse_mode='HTML')
    return st.NAXT_DATA


def get_naxt_data(update: Update, context: CallbackContext):
    data_size = update.message.text
    if data_size.isdigit() and int(data_size) >= 0:
        context.user_data['naxt_data_size'] = int(data_size)
        update.message.reply_html(
            text="<code>Bugungi plastig holatdagi savdo hajmini kiriting</code> [litr]"
        )
        return st.PLASTIG_DATA
    else:
        update.message.reply_text(
            text="<code>Bugungi naxt holatdagi savdo hajmini kiriting</code>",
            parse_mode='HTML'
        )


def fuel_column_pointer(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    fuel_columns = OrganizationFuelColumns.objects.filter(organization=user.organization)
    if not fuel_columns:
        update.message.reply_html(
            text="<code>Ma'lumotlar saqlab qo'yildi</code>"
        )
        return st.FINISHED
    msg = ""
    for fuel_col in fuel_columns:
        fuel_data = FuelColumnPointer.objects.filter(organ=user.organization, fuel_column=fuel_col.fuel_column,
                                                     created_at__date=timezone.now().date())
        if fuel_data:
            msg += f"{fuel_col.fuel_column.title} - ✅\n"
        else:
            msg += f"{fuel_col.fuel_column.title} ❗️\n"
    user_fuel_column_txt = f"""
<b>{user.fullname}</b> - <code>{user.organization.title}</code> tashkiloti uchun:

<i>Bugungi hisobotlarni kiriting</i>

{msg}

Yuqoridagi yoqilg'i ustunlari uchun ma'lumotlar kiritish uchun pastdagi tugmalardan birini tanlang 👇
                """
    update.message.reply_html(text=user_fuel_column_txt,
                              reply_markup=kb.organ_fuel_columns(fuel_columns, user.language))
    return st.ADD_TODAY_FUEL_COLUMN


def get_today_fuel_column(update: Update, context: CallbackContext):
    query = update.callback_query
    # user = User.objects.get(chat_id=update.effective_chat.id)
    fuel_column = FuelColumn.objects.get(id=query.data)
    context.user_data['fuel_column'] = fuel_column
    query.delete_message()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"<code>Kun oxiridagi {fuel_column.title} - kolonka raqamini kiriting</code>",
                             parse_mode='HTML')
    return st.ADD_FUEL_COLUMN_NUM


def get_fuel_column_num(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    msg = update.message.text
    if msg.isdigit() and int(msg) > 0:
        context.user_data['column_num'] = int(msg)
        fuel_column = context.user_data['fuel_column']
        FuelColumnPointer.objects.create(
            organ=user.organization,
            fuel_column=fuel_column,
            size_last=int(msg),
            size_first=FuelColumnPointer.objects.filter(organ=user.organization,
                                                        fuel_column=fuel_column).last().size_last
        )
        fuel_columns = OrganizationFuelColumns.objects.filter(organization=user.organization)
        msg = ""
        for fuel_col in fuel_columns:
            fuel_data = FuelColumnPointer.objects.filter(organ=user.organization, fuel_column=fuel_col.fuel_column,
                                                         created_at__date=timezone.now().date())
            if fuel_data:
                msg += f"{fuel_col.fuel_column.title} - ✅\n"
            else:
                msg += f"{fuel_col.fuel_column.title} ❗️\n"
        user_fuel_column_txt = f"""
<b>{user.fullname}</b> - <code>{user.organization.title}</code> tashkiloti uchun:

<i>Bugungi hisobotlarni kiriting</i>

{msg}

Yuqoridagi yoqilg'i ustunlari uchun ma'lumotlar kiritish uchun pastdagi tugmalardan birini tanlang 👇

        """
        update.message.reply_html(text=user_fuel_column_txt,
                                  reply_markup=kb.organ_fuel_columns(fuel_columns, user.language))
        return st.ADD_TODAY_FUEL_COLUMN
    else:
        update.message.reply_text(
            text="<code>Kun oxiridagi kolonka raqamini kiriting</code>",
            parse_mode='HTML'
        )


def get_plastig_data(update: Update, context: CallbackContext):
    data_size = update.message.text
    user = User.objects.get(chat_id=update.effective_user.id)
    if data_size.isdigit() and int(data_size) >= 0:
        context.user_data['plastig_data_size'] = int(data_size)
        naxt_data_size = context.user_data['naxt_data_size']
        fuel_type = context.user_data['fuel_type']
        SaleFuel.objects.create(
            fuel_type=fuel_type,
            cash_size=float(naxt_data_size),
            card_size=float(data_size),
        )
        organization_fuel_types = OrganizationFuelTypes.objects.filter(organization=user.organization)
        msg, i = "", 0
        for org_fuel_type in organization_fuel_types:
            fuel_data = SaleFuel.objects.filter(fuel_type=org_fuel_type.fuel_type,
                                                created_at__date=timezone.now().date())
            if fuel_data:
                i += 1
                msg += f"{org_fuel_type.fuel_type.title} - ✅\n"
            else:
                msg += f"{org_fuel_type.fuel_type.title} ❗️\n"
        if i == organization_fuel_types.count():
            return fuel_column_pointer(update, context)
        user_fuel_type_txt = f"""
<b>{user.fullname}</b> - <code>{user.organization.title}</code> tashkiloti uchun:

<i>Bugungi hisobotlarni kiriting</i>

{msg}

Yuqoridagi yoqilg'ilar uchun ma'lumotlar kiritish uchun pastdagi tugmalardan birini tanlang 👇
        """
        update.message.reply_html(text=user_fuel_type_txt,
                                  reply_markup=kb.organ_fuel_types(organization_fuel_types, user.language))
        return st.ADD_TODAY_DATA
    else:
        update.message.reply_text(
            text="<code>Bugungi plastig holatdagi savdo hajmini kiriting</code>",
            parse_mode='HTML'
        )


def get_data_type_first(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    update.message.reply_text('-_-',
                              reply_markup=ReplyKeyboardRemove())
    payment_types = PaymentType.objects.filter(is_active=True)
    update.message.reply_text(msg_txt.choose_payment_type.get(user.language),
                              reply_markup=kb.fuel_columns(payment_types, user.language))
    return st.CHOOSE_PAYMENT_TYPE


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
        update.message.reply_html(
            text="<code>Yuborgan ma'lumotlaringiz saqlab qo'yildi</code>"
        )
        update.message.reply_text(
            msg_txt.choose_back_type.get(user.language),
            reply_markup=kb.back_types(user.language)
        )
        return st.SUCCES
    else:
        update.message.reply_text(
            text=msg_txt.fuel_price_today.get(user.language))
    return st.SELL_FUEL_SIZE


def get_data_type_last(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.effective_user.id)
    update.message.reply_text('-_-',
                              reply_markup=ReplyKeyboardRemove())
    columns = FuelColumn.objects.filter(is_active=True)
    update.message.reply_text(msg_txt.choose_fuel_column.get(user.language),
                              reply_markup=kb.fuel_columns(columns, user.language))
    return st.CHOOSE_FUEL_COLUMN
