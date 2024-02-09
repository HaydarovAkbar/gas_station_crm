try:
    from .base import start, k_fuel_column, k_choose_column, k_change_column_first, k_fuel_type, k_get_fuel_type, k_input_column_num, k_back, k_input_column_num_last, k_change_column_last
    from .leader import leader
    from .admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, \
        get_user_role, change_user, change_user_id, change_user_role
except ImportError as e:
    print(e)
    from base import start, k_fuel_column, k_choose_column, k_change_column_first, k_fuel_type, k_get_fuel_type, k_input_column_num, k_back, k_input_column_num_last, k_change_column_last
    from leader import leader
    from admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, get_user_role, \
        change_user, change_user_id, change_user_role

    print('ImportError')
