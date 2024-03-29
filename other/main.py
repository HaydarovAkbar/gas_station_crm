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
from methods.admin.views import admin, add_organization, get_organization_name, add_user, get_organization_phone, \
    get_organization_address, get_organization_leader, delete_organization, get_organization_id, \
    organization_fuel_types, organization_fuel_columns, get_user_id, get_user_organization, \
    change_user_role, delete_user, get_user_id_delete
from methods.kassir.views import send_night_notification, get_start, get_fuel_type, get_data_type_first, \
    get_data_type_last, get_fuel_price_today, get_sell_fuel_size, get_naxt_data, \
    get_fuel_column_num, get_plastig_data, get_today_fuel_column
from states import States as st
from datetime import time

from methods.kassir.texts import KeyboardsTexts as kas_txt
from methods.dictionary import AdminButton as bt

bt = bt()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True, workers=500)
app = updater.dispatcher

job = updater.job_queue

job.run_daily(send_night_notification, days=(0, 1, 2, 3, 4, 5, 6),
              time=time(hour=20, minute=48, second=00, tzinfo=pytz.timezone('Asia/Tashkent')), )

handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        MessageHandler(Filters.regex('^(' + kas_txt.start['uz'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['ru'] + ')$'), get_start),
        MessageHandler(Filters.regex('^(' + kas_txt.start['en'] + ')$'), get_start),
    ],
    states={
        st.NOTSTART: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
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

            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][1] + ')$'), get_data_type_last),
        ],
        st.ADD_TODAY_FUEL_COLUMN: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_today_fuel_column),
        ],
        st.ADD_FUEL_PRICE_TODAY: [
            CommandHandler('start', start),

            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][1] + ')$'), get_data_type_last),

            MessageHandler(Filters.text, get_fuel_price_today)
        ],
        st.SELL_FUEL_SIZE: [
            CommandHandler('start', start),

            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['uz'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['ru'][1] + ')$'), get_data_type_last),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][0] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.data_types['en'][1] + ')$'), get_data_type_last),

            MessageHandler(Filters.text, get_sell_fuel_size)
        ],
        st.NAXT_DATA: [
            CommandHandler('start', start),
            MessageHandler(Filters.text, get_naxt_data)
        ],
        st.PLASTIG_DATA: [
            CommandHandler('start', start),
            MessageHandler(Filters.text, get_plastig_data)
        ],
        st.SUCCES: [

            CommandHandler('start', start),

            MessageHandler(Filters.regex('^(' + kas_txt.back_types['uz'][0] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['uz'][1] + ')$'), get_naxt_data),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['uz'][2] + ')$'), get_data_type_first),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['ru'][1] + ')$'), get_naxt_data),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['ru'][0] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['ru'][1] + ')$'), get_data_type_first),

            MessageHandler(Filters.regex('^(' + kas_txt.back_types['en'][0] + ')$'), get_start),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['en'][1] + ')$'), get_naxt_data),
            MessageHandler(Filters.regex('^(' + kas_txt.back_types['en'][2] + ')$'), get_data_type_first),
        ],
        st.ADD_FUEL_COLUMN_NUM: [
            MessageHandler(Filters.text, get_fuel_column_num)
        ],

        st.ADMIN: [
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][0] + ')$'), add_user),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][1] + ')$'), add_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][2] + ')$'), delete_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][3] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][4] + ')$'), delete_user),

            MessageHandler(Filters.regex('^(' + bt.adm_menu['ru'][0] + ')$'), add_user),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['ru'][1] + ')$'), add_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['ru'][2] + ')$'), delete_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['ru'][3] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][4] + ')$'), delete_user),

            MessageHandler(Filters.regex('^(' + bt.adm_menu['en'][0] + ')$'), add_user),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['en'][1] + ')$'), add_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['en'][2] + ')$'), delete_organization),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['en'][3] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + bt.adm_menu['uz'][4] + ')$'), delete_user),
        ],
        st.ADD_ORGANIZATION: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            MessageHandler(Filters.text, get_organization_name),
        ],
        st.ADD_ORGANIZATION_PHONE: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            MessageHandler(Filters.text, get_organization_phone),
        ],
        st.ADD_ORGANIZATION_ADDRESS: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            MessageHandler(Filters.text, get_organization_address),
        ],
        st.ADD_ORGANIZATION_LEADER: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            MessageHandler(Filters.text, get_organization_leader),
        ],
        st.ORGANIZATION_FUEL_TYPE: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            CallbackQueryHandler(organization_fuel_types),
        ],
        st.ORGANIZATION_FUEL_COLUMN: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
            MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),

            CallbackQueryHandler(organization_fuel_columns),
        ],
        st.DELETE_ORGANIZATION: [
            CommandHandler('start', start),
            CommandHandler('admin', admin),
            CallbackQueryHandler(get_organization_id),
        ],
        st.ADD_USER: [CommandHandler('start', start),
                      CommandHandler('admin', admin),
                      # CommandHandler('leader', leader),
                      CallbackQueryHandler(get_user_id),
                      ],
        st.CHOOSE_ORGANIZATION: [CommandHandler('start', start),
                                 CommandHandler('admin', admin),
                                 CallbackQueryHandler(get_user_organization),
                                 ],

        st.USER_ROLE: [CommandHandler('start', start),
                       CommandHandler('admin', admin),
                       # CommandHandler('leader', leader),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),
                       CallbackQueryHandler(change_user_role),
                       ],
        st.USER_CONF: [CommandHandler('start', start),
                       CommandHandler('admin', admin),
                       # CommandHandler('leader', leader),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
                       MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),
                       MessageHandler(Filters.text, change_user_role),
                       ],
        st.DELETE_USER: [CommandHandler('start', start),
                         CommandHandler('admin', admin),
                         # CommandHandler('leader', leader),
                         MessageHandler(Filters.regex('^(' + kas_txt.back['uz'] + ')$'), admin),
                         MessageHandler(Filters.regex('^(' + kas_txt.back['ru'] + ')$'), admin),
                         MessageHandler(Filters.regex('^(' + kas_txt.back['en'] + ')$'), admin),
                         MessageHandler(Filters.text, get_user_id_delete),
                         ],
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
