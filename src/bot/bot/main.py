from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, ConversationHandler


def run():
    bot.set_webhook(settings.HOST + '/bot/')

bot: Bot = Bot(token=settings.TOKEN)

dispatcher = Dispatcher(bot, None)


def help(update: Update, context):
    msg_txt = """
<b>Botdan foydalanish bo'yicha qo'llanma 🆘</b>
<i>
1️⃣ Kanalga admin qilish
2️⃣ Kanalga biriktirilgan guruhga admin qilish
3️⃣ Guruhni <code>ommaviy guruh</code> qilish
4️⃣ Kanal va guruh linklarini pr.sport.uz tizimiga kiritish
</i>
"""
    update.message.reply_html(msg_txt)
    return True


# all_handler = MessageHandler(Filters.all, message)
help_handler = CommandHandler('help', help)

dispatcher.add_handler(help_handler)
# dispatcher.add_handler(all_handler)