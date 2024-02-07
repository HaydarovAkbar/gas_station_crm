try:
    from .base import start
    from .leader import leader
    from .admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id
except ImportError:
    from base import start
    from leader import leader
    from admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id
    print('ImportError')
