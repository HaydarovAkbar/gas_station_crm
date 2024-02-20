import sys

sys.dont_write_bytecode = True
# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from decouple import config
# Import your models for use in your script
import logging, pytz

TOKEN = config('TOKEN')
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from methods.core.views import start
from methods.kassir.views import send_night_notification
from states import States as st
from datetime import datetime, time

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True, workers=500)
app = updater.dispatcher

job = updater.job_queue


def send_message(context):
    context.bot.send_message(chat_id=758934089, text=f"Hello World {datetime.now()}")
    return 1


job.run_daily(send_message, days=(0, 1, 2, 3, 4, 5, 6),
              time=time(hour=17, minute=33, second=00, tzinfo=pytz.timezone('Asia/Tashkent')), )

job.run_daily(send_night_notification, days=(0, 1, 2, 3, 4, 5, 6),
              time=time(hour=18, minute=21, second=00, tzinfo=pytz.timezone('Asia/Tashkent')), )

handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        # CommandHandler('admin', admin)
    ],
    states={
        1: [
            CommandHandler('start', start),
            # CommandHandler('admin', admin),
            MessageHandler(Filters.text, start)
        ],
    },
    fallbacks=[
        CommandHandler('start', start),
        #        CommandHandler('admin', admin),
    ]
)

app.add_handler(handler=handler)

updater.start_polling()
print('started polling')
updater.idle()
