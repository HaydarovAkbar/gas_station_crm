from telegram import Update
from telegram.ext import CallbackContext

from bot.models import User


def start(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        User.objects.create(chat_id=tg_user.id, state_id=2, username=tg_user.username, fullname=tg_user.full_name)
        return 1
    update.message.reply_text('Salom')
