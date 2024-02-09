try:
    from .base import start, k_fuel_column
    from .leader import leader
    from .admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, \
        get_user_role, change_user, change_user_id, change_user_role
except ImportError:
    from base import start, k_fuel_column
    from leader import leader
    from admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, get_user_role, \
        change_user, change_user_id, change_user_role

    print('ImportError')
