from telegram import Update
from telegram.ext import CallbackContext

from bot.models import User, UserTypes


def leader(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    user = User.objects.filter(chat_id=tg_user.id, state__id=1)
    if not user.exists():
        return 1
    user = user.first()
    user_type = UserTypes.objects.get(title='RAHBAR')
    if user_type.id in user.roles.values_list('id', flat=True):
        update.message.reply_text('Rahbar Salom')
    else:
        update.message.reply_text('siz Rahbar emassiz')