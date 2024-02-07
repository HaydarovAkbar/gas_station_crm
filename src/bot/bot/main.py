from django.conf import settings as django_settings
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from .methods import *
from .static.base import Buttom as B
from .states import States as S
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def run():
    print('started webhook')
    bot.set_webhook(django_settings.HOST + '/bot/')


B = B()
S = S

bot: Bot = Bot(token=django_settings.TOKEN)

dispatcher = Dispatcher(bot, None)

handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        CommandHandler('leader', leader),
    ],
    states={
        S.ADMIN: [CommandHandler('start', start),
                  CommandHandler('admin', admin),
                  CommandHandler('leader', leader),
                  MessageHandler(Filters.regex('^(' + B.adm_menu['uz'][0] + ')$'), get_users),
                  MessageHandler(Filters.regex('^(' + B.adm_menu['uz'][1] + ')$'), settings),

                  MessageHandler(Filters.regex('^(' + B.adm_menu['ru'][0] + ')$'), get_users),
                  MessageHandler(Filters.regex('^(' + B.adm_menu['ru'][1] + ')$'), settings),

                  MessageHandler(Filters.regex('^(' + B.adm_menu['en'][0] + ')$'), get_users),
                  MessageHandler(Filters.regex('^(' + B.adm_menu['en'][1] + ')$'), settings),
                  ],
        S.GET_USERS: [CommandHandler('start', start),
                      CommandHandler('admin', admin),
                      CommandHandler('leader', leader),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][0] + ')$'), get_users),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][1] + ')$'), settings),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][2] + ')$'), back),

                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][0] + ')$'), get_users),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][1] + ')$'), settings),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][2] + ')$'), back),

                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['en'][0] + ')$'), get_users),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['en'][1] + ')$'), settings),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['en'][2] + ')$'), back),
                      ],

        S.ADMIN_SETTINGS: [CommandHandler('start', start),
                           CommandHandler('admin', admin),
                           CommandHandler('leader', leader),
                           MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][0] + ')$'), change_language),
                           MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][1] + ')$'), back),

                           MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][0] + ')$'), change_language),
                           MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][1] + ')$'), back),

                           MessageHandler(Filters.regex('^(' + B.adm_settings['en'][0] + ')$'), change_language),
                           MessageHandler(Filters.regex('^(' + B.adm_settings['en'][1] + ')$'), back),
                           ],
        S.CHANGE_LANG: [CommandHandler('start', start),
                        CommandHandler('admin', admin),
                        CommandHandler('leader', leader),
                        CallbackQueryHandler(get_lang),
                        ],

    },
    fallbacks=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        CommandHandler('leader', leader),
    ]
)

dispatcher.add_handler(handler)
