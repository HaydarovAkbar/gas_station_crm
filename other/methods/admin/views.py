from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from states import States as S
from db.models import User, Organization, FuelType, FuelColumn, FuelStorage, Fuel, FuelColumnPointer
from methods.admin.keyboards import KeyboardsAdmin as K
from ..dictionary import AdmTexts as T


def admin(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.get(chat_id=tg_user.id, is_active=True)
    if not user.is_admin:
        return 1
    user_lang = user.language if user.language else 'uz'
    update.message.reply_text(T().start[user_lang].format(tg_user.full_name), reply_markup=K().get_menu(user_lang))
    return S.ADMIN


def get_users(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        update.message.reply_html(T().get_user[user_lang],
                                  reply_markup=K().get_user_menu(user_lang))
        return S.GET_USERS


def settings(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')

    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        update.message.reply_html(T().get_user[user_lang], reply_markup=K().adm_settings(user_lang))
        return S.ADMIN_SETTINGS


def change_language(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        update.message.reply_html(T().change_language[user_lang], reply_markup=K().get_lang())
        return S.CHANGE_LANG


def get_lang(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer(text="Til o'zgartirildi: {}".format(query.data))
    change_lang = query.data
    user = User.objects.get(chat_id=query.from_user.id)
    user.language = change_lang
    user.save()
    query.message.delete(timeout=1)
    tg_user = query.from_user
    context.bot.send_message(chat_id=query.from_user.id, text=T().start[change_lang].format(tg_user.full_name),
                             reply_markup=K().get_menu(change_lang))
    return S.ADMIN


def back(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        update.message.reply_text(T().start[user_lang].format(tg_user.full_name), reply_markup=K().get_menu(user_lang))
        return S.ADMIN


def add_user(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        user_list = User.objects.filter(state__id=2).order_by('-created_at')[0:10]
        update.message.reply_text('...', reply_markup=ReplyKeyboardRemove())
        update.message.reply_html(T().add_user[user_lang], reply_markup=K().user_list(user_list))
        return S.ADD_USER


def get_user_id(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.data
    user_db = User.objects.get(chat_id=query.from_user.id)
    query.delete_message()
    if user_id == 'back':
        context.bot.send_message(chat_id=query.from_user.id, text=T().start[user_db.language].format(user_db.fullname),
                                 reply_markup=K().get_menu(user_db.language))
        return S.ADMIN
    context.chat_data['user_id'] = user_id
    context.bot.send_message(chat_id=query.from_user.id,
                             text=T().roles[user_db.language],
                             reply_markup=K().roles())
    return S.USER_ROLE


def get_user_role(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    tg_user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not tg_user.exists():
        return 1
    tg_user = tg_user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in tg_user.roles.values_list('id', flat=True):
        user_lang = tg_user.language if tg_user.language else 'uz'
        user_id = context.chat_data['user_id']
        user = User.objects.get(chat_id=user_id)
        organization = tg_user.organization.first()
        if update.message.text == T().adm_roles[user_lang][0]:
            user.roles.add(UserTypes.objects.get(title='ADMIN'))
            user.state = State.objects.get(id=1)
            user.organization.set([organization])
            user.save()
            update.message.reply_text('Admin roliga qo\'shildi', reply_markup=K().get_menu(user_lang))
        elif update.message.text == T().adm_roles[user_lang][1]:
            user.roles.add(UserTypes.objects.get(title='KASSIR'))
            user.state = State.objects.get(id=1)
            user.organization.set([organization])
            user.save()
            update.message.reply_text('Kassir roliga qo\'shildi', reply_markup=K().get_menu(user_lang))
        elif update.message.text == T().adm_roles[user_lang][2]:
            user.roles.add(UserTypes.objects.get(title='KASSIR'))
            user.roles.add(UserTypes.objects.get(title='ADMIN'))
            user.state = State.objects.get(id=1)
            user.organization.set([organization])
            user.save()
            update.message.reply_text('Admin va Kassir roliga qo\'shildi', reply_markup=K().get_menu(user_lang))
        else:
            update.message.reply_text('Xatolik')
        return S.ADMIN


def change_user(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        user_list = User.objects.filter(state__id=1).order_by('-created_at')[0:20]
        update.message.reply_text('...', reply_markup=ReplyKeyboardRemove())
        update.message.reply_html(T().add_user[user_lang], reply_markup=K().user_list(user_list))
        return S.CHANGED_USER


def change_user_id(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.data
    user_db = User.objects.get(chat_id=query.from_user.id)
    query.delete_message()
    if user_id == 'back':
        context.bot.send_message(chat_id=query.from_user.id, text=T().start[user_db.language].format(user_db.fullname),
                                 reply_markup=K().get_menu(user_db.language))
        return S.ADMIN
    context.chat_data['user_id'] = user_id
    user_fullname = User.objects.get(chat_id=user_id).fullname
    user_roles = User.objects.get(chat_id=user_id).roles.values_list('title', flat=True)
    user_lang = User.objects.get(chat_id=query.from_user.id).language
    context.bot.send_message(chat_id=query.from_user.id,
                             text=T().change_user[user_lang].format(user_fullname),
                             reply_markup=K().user_change(user_roles, user_lang))
    return S.USER_CONF


def change_user_role(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        user_id = context.chat_data['user_id']
        user = User.objects.get(chat_id=user_id)
        if update.message.text == T().adm_roles[user_lang][0]:
            user.roles.clear()
            user.roles.add(UserTypes.objects.get(title='ADMIN'))
            user.save()
            update.message.reply_text('Adminga o\'zgartirildi', reply_markup=K().get_menu(user_lang))
        elif update.message.text == T().adm_roles[user_lang][1]:
            user.roles.clear()
            user.roles.add(UserTypes.objects.get(title='KASSIR'))
            user.save()
            update.message.reply_text('Kassirga o\'zgartirildi', reply_markup=K().get_menu(user_lang))
        elif update.message.text == T().adm_roles[user_lang][2]:
            user.roles.add(UserTypes.objects.get(title='KASSIR'))
            user.roles.add(UserTypes.objects.get(title='ADMIN'))
            user.save()
            update.message.reply_text('Admin va Kassir roliga o\'zgartirildi', reply_markup=K().get_menu(user_lang))
        elif update.message.text == T().adm_roles[user_lang][4]:
            user.delete()
            update.message.reply_text('O\'chirildi bu foydalanuvchi', reply_markup=K().get_menu(user_lang))
        else:
            update.message.reply_text('Xatolik')
        return S.ADMIN
