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
        update.message.reply_text('sozlamalar')
        return S.ADMIN