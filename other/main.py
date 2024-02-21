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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from methods.core.views import start
from methods.kassir.views import send_night_notification, get_start, get_fuel_type, get_data_type
from states import States as st
from datetime import datetime, time

from methods.kassir.texts import KeyboardsTexts as kas_txt

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True, workers=500)
app = updater.dispatcher

job = updater.job_queue

job.run_daily(send_night_notification, days=(0, 1, 2, 3, 4, 5, 6),
              time=time(hour=14, minute=42, second=00, tzinfo=pytz.timezone('Asia/Tashkent')), )

handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        # CommandHandler('admin', admin)
        MessageHandler(Filters.regex('^(' + kas_txt.start['uz'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['ru'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['en'] + ')$'), get_start),
    ],
    states={
        st.NOTSTART: [
            CommandHandler('start', start),
            # CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.start['uz'] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.start['ru'] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.start['en'] + ')$'), get_start),
        ],
        st.ADD_TODAY_DATA: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_fuel_type),
        ],
        st.DATA_TYPE: [
            CommandHandler('start', start),

            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][0] + ')$'), get_data_type),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][1] + ')$'), get_data_type),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][0] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][1] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][0] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][1] + ')$'), get_start),
        ]
    },
    fallbacks=[
        CommandHandler('start', start),
        #        CommandHandler('admin', admin),

        MessageHandler(Filters.regex('^(' + kas_txt.start['uz'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['ru'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['en'] + ')$'), get_start),
    ]
)

app.add_handler(handler=handler)

updater.start_polling()
print('started polling')
updater.idle()
