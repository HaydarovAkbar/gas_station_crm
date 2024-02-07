from telegram import Update
from telegram.ext import CallbackContext

from ..states import States as S
from ..keyboards import KeyboardsAdmin as K
from ..static.base import AdmTexts as T

from bot.models import User, UserTypes


def admin(update: Update, context: CallbackContext):
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
    else:
        update.message.reply_text('siz Admin emassiz')


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
        update.message.reply_text(T().add_user(user_lang), reply_markup=K().back(user_lang))
        return S.ADD_USER


def get_user_id(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language if user.language else 'uz'
        if update.message.text.isdigit():
            user_id = update.message.text
        else:
            user_id = update.message.forward_from.id
        print(user_id)
        user = User.objects.filter(chat_id=user_id)
        context.chat_data['user_id'] = user_id
        if user.exists():
            update.message.reply_text(T().user_already_exists[user_lang], reply_markup=K().back(user_lang))
        else:
            User.objects.create(chat_id=user_id, state_id=1)
            update.message.reply_text(T().user_added[user_lang], reply_markup=K().roles(user_lang))
            return S.USER_ROLE
        update.message.reply_text(T().add_user(user_lang), reply_markup=K().back(user_lang))
        return S.ADD_USER
    else:
        update.message.reply_text('siz Admin emassiz')


def get_user_role(update: Update, context: CallbackContext):
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
            user.roles.add(UserTypes.objects.get(title='ADMIN'))
            user.save()
            update.message.reply_text('Admin qo\'shildi')
        elif update.message.text == T().adm_roles[user_lang][1]:
            user.roles.add(UserTypes.objects.get(title='CASHIER'))
            user.save()
            update.message.reply_text('Kassir qo\'shildi')
        else:
            update.message.reply_text('Xatolik')
        return S.ADMIN
    else:
        update.message.reply_text('siz Admin emassiz')
