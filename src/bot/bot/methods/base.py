from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from ..static.base import KTexts as T
from ..keyboards.base import KeyboardsUser as K
from ..states import States as S

from datetime import datetime

from bot.models import User, UserTypes, FuelColumn, FuelColumnPointer, Fuel, FuelType, FuelStorage, PaymentType, SaleFuel


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
        context.bot.send_message(chat_id=tg_user.id, text=T().fuel_column[user_lang], parse_mode="HTML",
                                 reply_markup=K().fuel_columns(fuel_columns, user_lang))
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
        column_pointer = FuelColumnPointer.objects.filter(fuel_column=column, created_at__date=datetime.now().date())
        if column_pointer.exists() and column_pointer.first().size_first and column_pointer.first().size_last:
            context.bot.send_message(chat_id=tg_user.id,
                                     text=T().column_pointer_already_exist[user_lang].format(
                                         column_pointer.first().size_first, column_pointer.first().size_last),
                                     parse_mode="HTML",
                                     reply_markup=K().back(user_lang))
            return S.CHANGE_COLUMN
        context.bot.send_message(chat_id=tg_user.id,
                                 text=T().column_chosen[user_lang].format(fuel_type.title, column.title),
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
        column = context.chat_data['column']
        column_pointer = FuelColumnPointer.objects.filter(fuel_column=column, created_at__date=datetime.now().date())
        if column_pointer.exists() and column_pointer.first().size_first:
            update.message.reply_html(
                T().column_num_already_exist_1[user_lang].format(column_pointer.first().size_first),
                reply_markup=K().back(user_lang))
            return S.CHANGE_COLUMN_NUM
        else:
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
            fuel_column = context.chat_data['column']
            fuel_type = context.chat_data['fuel_type']
            today_fuel = Fuel.objects.filter(created_at__date=datetime.now().date())
            if not today_fuel.exists():
                fuelstorage = FuelStorage.objects.filter(fuel_type=fuel_type,
                                                         organization=user.organization.first()).last()
                fuel = Fuel()
                fuel.fuel_column = fuel_column
                fuel.fuel_type = fuel_type
                fuel.purchase = fuelstorage.input_price
                fuel.sale = fuelstorage.output_price
                fuel.balance = fuelstorage.output_price - fuelstorage.input_price
                fuel.day = datetime.now().date()
                fuel.save()
                fuel_column_pointer = FuelColumnPointer()
                fuel_column_pointer.fuel_column = fuel_column
                fuel_column_pointer.day = fuel
                fuel_column_pointer.size_first = column_num
                fuel_column_pointer.save()
                update.message.reply_html(T().column_num_success[user_lang], reply_markup=K().back(user_lang))
                return S.CHANGE_COLUMN_NUM
            else:
                today_fuel = today_fuel.first()
                fuel_column_pointer = FuelColumnPointer.objects.filter(fuel_column=context.chat_data['column'],
                                                                       day=today_fuel)
                if fuel_column_pointer.exists():
                    update.message.reply_html(
                        T().column_num_already_exist_1[user_lang].format(fuel_column_pointer.first().size_first),
                        reply_markup=K().back(user_lang))
                    return S.CHANGE_COLUMN_NUM
                else:
                    fuel_column_pointer = FuelColumnPointer()
                    fuel_column_pointer.fuel_column = fuel_column
                    fuel_column_pointer.day = today_fuel
                    fuel_column_pointer.size_first = column_num
                    fuel_column_pointer.save()
                    update.message.reply_html(T().column_num_success[user_lang], reply_markup=K().back(user_lang))
                    return S.CHANGE_COLUMN_NUM
        update.message.reply_html(T().column_num_error[user_lang], reply_markup=K().back(user_lang))
        return S.CHANGE_COLUMN_NUM


def k_change_column_last(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        column = context.chat_data['column']
        column_pointer = FuelColumnPointer.objects.filter(fuel_column=column, created_at__date=datetime.now().date())
        if column_pointer.exists() and column_pointer.first().size_last:
            update.message.reply_html(
                T().column_num_already_exist_2[user_lang].format(column_pointer.first().size_last),
                reply_markup=K().back(user_lang))
            return S.CHANGE_COLUMN_NUM_LAST
        else:
            update.message.reply_html(T().fuel_column_numbers[user_lang], reply_markup=K().back(user_lang))
            return S.CHANGE_COLUMN_NUM_LAST


def k_input_column_num_last(update: Update, context: CallbackContext):
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
            today_fuel = Fuel.objects.filter(created_at__date=datetime.now().date())
            if not today_fuel.exists():
                update.message.reply_html(T().column_num_error[user_lang], reply_markup=K().back(user_lang))
                return S.CHANGE_COLUMN_NUM_LAST
            else:
                today_fuel = today_fuel.first()
                fuel_column_pointer = FuelColumnPointer.objects.filter(fuel_column=context.chat_data['column'],
                                                                       day=today_fuel)
                if fuel_column_pointer.exists():
                    fuel_column_pointer = fuel_column_pointer.first()
                    fuel_column_pointer.size_last = column_num
                    fuel_column_pointer.save()
                    update.message.reply_html(T().column_num_success[user_lang], reply_markup=K().back(user_lang))
                    return S.CHANGE_COLUMN_NUM_LAST
                else:
                    update.message.reply_html(T().column_num_add_first[user_lang], reply_markup=K().back(user_lang))
                    return S.CHANGE_COLUMN_NUM_LAST
        update.message.reply_html(T().column_num_add_first[user_lang], reply_markup=K().back(user_lang))
        return S.CHANGE_COLUMN_NUM_LAST


def k_back(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    update.message.reply_html(T().start[user_lang].format(user.fullname), reply_markup=K().get_menu(user_lang))
    return S.START


def k_sale_fuel(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        fuel_type = FuelType.objects.filter(state__id=1)
        update.message.reply_text('👇👇', reply_markup=ReplyKeyboardRemove())
        update.message.reply_html(T().fuel_type[user_lang], reply_markup=K().fuel_types(fuel_type, user_lang))
        return S.FUEL_TYPE_SALE


def k_sale_fuel_type(update: Update, context: CallbackContext):
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
        payment_type = PaymentType.objects.filter(state__id=1)
        context.bot.send_message(chat_id=tg_user.id, text=T().choose_payment_type[user_lang], parse_mode="HTML",
                                 reply_markup=K().fuel_columns(payment_type, user_lang))
        return S.FUEL_COLUMN_SALE_PT


def k_fuel_column_sale(update: Update, context: CallbackContext):
    tg_user = update.callback_query.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        query = update.callback_query
        if query.data == 'back':
            fuel_type = FuelType.objects.filter(state__id=1)
            query.message.delete()
            context.bot.send_message(chat_id=tg_user.id, text=T().fuel_type[user_lang],
                                     parse_mode="HTML",
                                     reply_markup=K().fuel_types(fuel_type, user_lang))
            return S.FUEL_TYPE_SALE
        else:
            payment_type = PaymentType.objects.get(id=query.data)
            context.chat_data['payment_type'] = payment_type
            query.message.delete()
            context.bot.send_message(chat_id=tg_user.id, text=T().fuel_size_input[user_lang], parse_mode="HTML",
                                     reply_markup=K().back(user_lang))
            return S.FUEL_SALE_SIZE


def k_fuel_sale(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        fuel_size = update.message.text
        if fuel_size.isdigit():
            fuel_type = context.chat_data['fuel_type']
            payment_type = context.chat_data['payment_type']
            today_fuel = Fuel.objects.filter(created_at__date=datetime.now().date())
            print(today_fuel, 'today_fuel')
            if today_fuel.exists():
                fuel = today_fuel.first()
                print(fuel, 'fuel2')
                SaleFuel.objects.create(day=fuel, fuel_type=fuel_type, payment_type=payment_type, size=float(fuel_size))
                update.message.reply_html(T().fuel_size_added_success[user_lang], reply_markup=K().back(user_lang))
                return S.FUEL_SALE_SIZE
            else:
                fuel = Fuel.objects.create(fuel_type=fuel_type, day=datetime.now().date())
                print(fuel, 'fuel')
                fuel.fuel_type = fuel_type
                fuel.day = datetime.now().date()
                fuel.save()
                sale_fuel = SaleFuel()
                sale_fuel.day = fuel
                sale_fuel.fuel_type = fuel_type
                sale_fuel.payment_type = payment_type
                sale_fuel.size = float(fuel_size)
                sale_fuel.save()
                update.message.reply_html(T().fuel_size_added_success[user_lang], reply_markup=K().back(user_lang))
                return S.FUEL_SALE_SIZE
        update.message.reply_html(T().fuel_size_error[user_lang], reply_markup=K().back(user_lang))
        return S.FUEL_SALE_SIZE