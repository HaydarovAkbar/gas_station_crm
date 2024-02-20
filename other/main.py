import sys

sys.dont_write_bytecode = True
# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from decouple import config
# Import your models for use in your script
import logging

TOKEN = config('TOKEN')
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from methods.core.views import start, get_fullname
from methods.admin.views import admin
from states import States as st

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

update = Updater(token=TOKEN, use_context=True, workers=500)
app = update.dispatcher

handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  CommandHandler('admin', admin)
                  ],
    states={
        st.get_fullname: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.text, get_fullname)],
    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('admin', admin), ]
)

app.add_handler(handler=handler)

update.start_polling()
print('started polling')
update.idle()
