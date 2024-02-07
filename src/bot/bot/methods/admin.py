from telegram import Update
from telegram.ext import CallbackContext

from ..states import States as S
from ..keyboards import KeyboardsAdmin as K

from bot.models import User, UserTypes


def admin(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_text('Admin xush kelibsiz menyudan buyruqlarni tanlang!', reply_markup=K().get_menu())
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
        update.message.reply_text('Foydalanuvchilarni boshqarish buyruqlarini tanlang',
                                  reply_markup=K().get_user_menu())
        return S.GET_USERS


def settings(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')

    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_text('Sozlamalar menyusidan buyruqlarni tanlang!', reply_markup=K().adm_settings())
        return S.ADMIN_SETTINGS


def change_language(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='ADMIN')
    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_text('Tilni tanlang!', reply_markup=K().get_lang())
        return S.CHANGE_LANG


def get_lang(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer(text="Til o'zgartirildi: {}".format(query.data))
    change_lang = query.data
    user = User.objects.get(chat_id=query.from_user.id)
    user.language = change_lang
    user.save()
    query.message.delete(timeout=1)
    context.bot.send_message(chat_id=query.from_user.id, text="Menyuga qaytdik",
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
        update.message.reply_text('Admin xush kelibsiz menyudan buyruqlarni tanlang!', reply_markup=K().get_menu())
        return S.ADMIN
    else:
        update.message.reply_text('siz Admin emassiz')
        return S.ADMIN
