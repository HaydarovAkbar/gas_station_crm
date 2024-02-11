from django.conf import settings as django_settings
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from .methods import *
from .static.base import Button as B, KButtons as KB
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
KB = KB()

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
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][0] + ')$'), add_user),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][1] + ')$'), change_user),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['uz'][2] + ')$'), back),

                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][0] + ')$'), add_user),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][1] + ')$'), change_user),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['ru'][2] + ')$'), back),

                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['en'][0] + ')$'), add_user),
                      MessageHandler(Filters.regex('^(' + B.adm_user_menu['en'][1] + ')$'), change_user),
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
                        MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][0] + ')$'), change_language),
                        MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][1] + ')$'), back),

                        MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][0] + ')$'), change_language),
                        MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][1] + ')$'), back),

                        MessageHandler(Filters.regex('^(' + B.adm_settings['en'][0] + ')$'), change_language),
                        MessageHandler(Filters.regex('^(' + B.adm_settings['en'][1] + ')$'), back),
                        ],

        S.ADD_USER: [CommandHandler('start', start),
                     CommandHandler('admin', admin),
                     CommandHandler('leader', leader),
                     CallbackQueryHandler(get_user_id),
                     ],

        S.USER_ROLE: [CommandHandler('start', start),
                      CommandHandler('admin', admin),
                      CommandHandler('leader', leader),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][1] + ')$'), back),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][1] + ')$'), back),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['en'][1] + ')$'), back),
                      MessageHandler(Filters.text, get_user_role),
                      ],
        S.CHANGED_USER: [CommandHandler('start', start),
                         CommandHandler('admin', admin),
                         CommandHandler('leader', leader),
                         CallbackQueryHandler(change_user_id),
                         ],
        S.USER_CONF: [CommandHandler('start', start),
                      CommandHandler('admin', admin),
                      CommandHandler('leader', leader),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['uz'][1] + ')$'), back),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['ru'][1] + ')$'), back),
                      MessageHandler(Filters.regex('^(' + B.adm_settings['en'][1] + ')$'), back),
                      MessageHandler(Filters.text, change_user_role),
                      ],
        S.START: [CommandHandler('start', start),
                  CommandHandler('admin', admin),
                  CommandHandler('leader', leader),
                  MessageHandler(Filters.regex('^(' + KB.menu['uz'][0] + ')$'), k_fuel_type),
                  MessageHandler(Filters.regex('^(' + KB.menu['uz'][1] + ')$'), k_sale_fuel),
                  MessageHandler(Filters.regex('^(' + KB.menu['uz'][2] + ')$'), k_add_fuel_price_today),
                  MessageHandler(Filters.regex('^(' + KB.menu['uz'][3] + ')$'), k_settings),

                  MessageHandler(Filters.regex('^(' + KB.menu['ru'][0] + ')$'), k_fuel_type),
                  MessageHandler(Filters.regex('^(' + KB.menu['ru'][1] + ')$'), k_sale_fuel),
                  MessageHandler(Filters.regex('^(' + KB.menu['ru'][2] + ')$'), k_add_fuel_price_today),
                  MessageHandler(Filters.regex('^(' + KB.menu['ru'][3] + ')$'), k_settings),

                  MessageHandler(Filters.regex('^(' + KB.menu['en'][0] + ')$'), k_fuel_type),
                  MessageHandler(Filters.regex('^(' + KB.menu['en'][1] + ')$'), k_sale_fuel),
                  MessageHandler(Filters.regex('^(' + KB.menu['en'][2] + ')$'), k_add_fuel_price_today),
                  MessageHandler(Filters.regex('^(' + KB.menu['en'][3] + ')$'), k_settings),
                  ],
        S.KASSIR_SETTINGS: [CommandHandler('start', start),
                            CommandHandler('admin', admin),
                            CommandHandler('leader', leader),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['uz'][0] + ')$'), k_change_language),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['ru'][0] + ')$'), k_change_language),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['en'][0] + ')$'), k_change_language),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['uz'][1] + ')$'), k_back),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['ru'][1] + ')$'), k_back),
                            MessageHandler(Filters.regex('^(' + KB.k_settings['en'][1] + ')$'), k_back),
                            ],
        S.KASSIR_SETTINGS_CHANGE: [CommandHandler('start', start),
                                   CommandHandler('admin', admin),
                                   CommandHandler('leader', leader),
                                   CallbackQueryHandler(k_get_lang),
                                   ],
        S.FUEL_TYPE_PRICE: [CommandHandler('start', start),
                            CommandHandler('admin', admin),
                            CommandHandler('leader', leader),
                            CallbackQueryHandler(k_fuel_type_price),
                            ],
        S.FUEL_PRICE_INPUT: [CommandHandler('start', start),
                             CommandHandler('admin', admin),
                             CommandHandler('leader', leader),
                             MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][2] + ')$'), k_back),
                             MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][2] + ')$'), k_back),
                             MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][2] + ')$'), k_back),
                             MessageHandler(Filters.text, k_input_fuel_price),
                             ],
        S.FUEL_TYPE_SALE: [CommandHandler('start', start),
                           CommandHandler('admin', admin),
                           CommandHandler('leader', leader),
                           CallbackQueryHandler(k_sale_fuel_type),
                           ],
        S.FUEL_COLUMN_SALE_PT: [CommandHandler('start', start),
                                CommandHandler('admin', admin),
                                CommandHandler('leader', leader),
                                CallbackQueryHandler(k_fuel_column_sale),
                                ],
        S.FUEL_SALE_SIZE: [CommandHandler('start', start),
                           CommandHandler('admin', admin),
                           CommandHandler('leader', leader),
                           MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][2] + ')$'), k_back),
                           MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][2] + ')$'), k_back),
                           MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][2] + ')$'), k_back),
                           MessageHandler(Filters.text, k_fuel_sale),
                           ],
        S.FUEL_TYPE: [CommandHandler('start', start),
                      CommandHandler('admin', admin),
                      CommandHandler('leader', leader),
                      CallbackQueryHandler(k_get_fuel_type),
                      ],
        S.FUEL_COLUMN: [CommandHandler('start', start),
                        CommandHandler('admin', admin),
                        CommandHandler('leader', leader),
                        CallbackQueryHandler(k_choose_column),
                        ],
        S.CHANGE_COLUMN: [CommandHandler('start', start),
                          CommandHandler('admin', admin),
                          CommandHandler('leader', leader),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][0] + ')$'), k_change_column_first),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][1] + ')$'), k_change_column_last),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][2] + ')$'), k_back),

                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][0] + ')$'), k_change_column_first),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][1] + ')$'), k_change_column_last),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][2] + ')$'), k_back),

                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][0] + ')$'), k_change_column_first),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][1] + ')$'), k_change_column_last),
                          MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][2] + ')$'), k_back),
                          ],
        S.CHANGE_COLUMN_NUM: [CommandHandler('start', start),
                              CommandHandler('admin', admin),
                              CommandHandler('leader', leader),
                              MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][2] + ')$'), k_back),
                              MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][2] + ')$'), k_back),
                              MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][2] + ')$'), k_back),

                              MessageHandler(Filters.text, k_input_column_num),
                              ],
        S.CHANGE_COLUMN_NUM_LAST: [CommandHandler('start', start),
                                   CommandHandler('admin', admin),
                                   CommandHandler('leader', leader),
                                   MessageHandler(Filters.regex('^(' + KB.fuel_columns['uz'][2] + ')$'), k_back),
                                   MessageHandler(Filters.regex('^(' + KB.fuel_columns['ru'][2] + ')$'), k_back),
                                   MessageHandler(Filters.regex('^(' + KB.fuel_columns['en'][2] + ')$'), k_back),

                                   MessageHandler(Filters.text, k_input_column_num_last),
                                   ],

        S.LEADER: [CommandHandler('start', start),
                   CommandHandler('admin', admin),
                   CommandHandler('leader', leader),
                   ],
    },
    fallbacks=[
        CommandHandler('start', start),
        CommandHandler('admin', admin),
        CommandHandler('leader', leader),
    ]
)

dispatcher.add_handler(handler)
