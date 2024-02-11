try:
    from .base import (start, k_fuel_column, k_choose_column, k_change_column_first, k_fuel_type, k_get_fuel_type,
                       k_input_column_num, k_back, k_input_column_num_last, k_change_column_last, k_sale_fuel, k_sale_fuel_type,
                       k_fuel_column_sale, k_fuel_sale, k_add_fuel_price_today, k_fuel_type_price, k_input_fuel_price)
    from .leader import leader
    from .admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, \
        get_user_role, change_user, change_user_id, change_user_role
except ImportError as e:
    from base import (start, k_fuel_column, k_choose_column, k_change_column_first, k_fuel_type, k_get_fuel_type,
                      k_input_column_num, k_back, k_input_column_num_last, k_change_column_last, k_sale_fuel,
                      k_sale_fuel_type, k_fuel_column_sale, k_fuel_sale, k_add_fuel_price_today, k_fuel_type_price, k_input_fuel_price)
    from leader import leader
    from admin import admin, get_users, settings, back, change_language, get_lang, add_user, get_user_id, get_user_role, \
        change_user, change_user_id, change_user_role