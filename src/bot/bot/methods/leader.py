from telegram import Update
from telegram.ext import CallbackContext

from ..static.base import LeaderTexts as T
from ..keyboards.base import LeaderKeyboard as K
from ..states import States as S

from datetime import datetime

from bot.models import User, UserTypes, FuelType


def leader(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='RAHBAR')
    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_text(T().start[user.language].format(tg_user.full_name), reply_markup=K().get_menu(user.language))
        return S.LEADER


def input_fuel(update: Update, context: CallbackContext):
    user = User.objects.get(chat_id=update.message.from_user.id)
    user_type = UserTypes.objects.get(title='RAHBAR')
    if user_type.id in user.roles.values_list('id', flat=True):
        fuel_types = FuelType.objects.filter(state__id=1)
        update.message.reply_text(T().input_fuel_type[user.language], reply_markup=K().fuel_types(fuel_types, user.language))
        return S.L_FUEL_TYPE