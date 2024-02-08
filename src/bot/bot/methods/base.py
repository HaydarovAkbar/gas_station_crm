from telegram import Update
from telegram.ext import CallbackContext

from ..static.base import KTexts as T
from ..keyboards.base import KeyboardsUser as K
from ..states import States as S

from bot.models import User, UserTypes


def start(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        User.objects.create(chat_id=tg_user.id, state_id=2, username=tg_user.username, fullname=tg_user.full_name)
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='KASSIR')
    if user_type.id in user.roles.values_list('id', flat=True):
        user_lang = user.language
        update.message.reply_html(T().start[user_lang].format(user.fullname), reply_markup=K().get_menu(user_lang))
        return S.START


def k_manu(update: Update, context: CallbackContext):
    tg_user = update.message.from_user