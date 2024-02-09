from telegram import Update
from telegram.ext import CallbackContext

from ..static.base import KTexts as T
from ..keyboards.base import KeyboardsUser as K
from ..states import States as S

from bot.models import User, UserTypes, FuelColumn


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


def k_fuel_column(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_lang = user.language
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        fuel_columns = FuelColumn.objects.filter(state__id=1, organ=user.organization)
        update.message.reply_html(T().fuel_column[user_lang], reply_markup=K().fuel_columns(fuel_columns, user_lang))
        return S.FUEL_COLUMN
