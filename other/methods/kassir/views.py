from telegram.ext import CallbackContext
from telegram import Update

from .texts import MessageTexts as msg_txt
from .keryboards import KassirKeyboards as kb

from db.models import User


def send_night_notification(context: CallbackContext):
    users = User.objects.filter(is_active=True, position__icontains='KASSIR')
    print(users)
    for user in users:
        context.bot.send_message(
            chat_id=user.chat_id,
            text=msg_txt.night_notification[user.lang],
            reply_markup=kb.back(user.lang)
        )
