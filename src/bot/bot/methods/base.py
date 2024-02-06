from telegram import Update
from telegram.ext import CallbackContext

from bot.models import User


def start(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    update.message.reply_text('Salom')
