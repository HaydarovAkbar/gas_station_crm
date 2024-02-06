from django.conf import settings
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler

from .methods import *


def run():
    bot.set_webhook(settings.HOST + '/bot/')


bot: Bot = Bot(token=settings.TOKEN)

dispatcher = Dispatcher(bot, None)

handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        CommandHandler('leader', leader),
    ],
    states={
        1: [CommandHandler('start', start),
            CommandHandler('admin', admin),
            CommandHandler('leader', leader),
            ]
    },
    fallbacks=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        CommandHandler('leader', leader),
    ]
)

dispatcher.add_handler(handler)
