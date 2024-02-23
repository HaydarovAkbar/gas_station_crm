class AdminKeyboardMessage:
    menu = {
        'uz': [""]
    }


class AdminButton:
    adm_menu = {
        'uz': ["👤 Foydalanuvchi Boshqaruvi", "⚙️ Sozlamalar"],
        'ru': ["👤 Управление Пользователями", "⚙️ Настройки"],
        'en': ["👤 User Management", "⚙️ Settings"]
    }
    adm_user_menu = {
        'uz': ["✳️ Aktivlashtirish", "⛔️ Tahrirlash", "⬅️ Orqaga"],
        'ru': ["✳️ Активировать", "⛔️ Редактировать", "⬅️ Назад"],
        'en': ["✳️ Activate", "⛔️ Edit", "⬅️ Back"]
    }
    adm_settings = {
        'uz': ["Tilni o'zgartirish 🌐", "⬅️ Orqaga"],
        'ru': ["Изменить язык 🌐", "⬅️ Orqaga"],
        'en': ["Change language 🌐", "⬅️ Orqaga"]
    }
    adm_roles = {
        'uz': ["Admin 👮‍♀️", "Kassir 👨🏻‍💻", "Admin va Kassir", "⬅️ Orqaga", "O'chirish 🪓"],
        'ru': ["Админ 👮‍♀️", "Кассир 👨🏻‍💻", "Админ️ и Кассир", "⬅️ Назад", "Удалить 🪓"],
        'en': ["Admin 👮‍♀️", "Cashier 👨🏻‍💻", "Admin and Cashier", "⬅️ Back", "Delete 🪓"]
    }

    inline_back = {
        'uz': "⬅️ Orqaga",
        'ru': "⬅️ Назад",
        'en': "⬅️ Back"
    }


class AdmTexts:
    start = {
        'uz': 'Assalom alaykum, {}!\n\nBotdan foydalanishingiz mumkin!',
        'ru': 'Здравствуйте, {}!\n\nВы можете использовать бота!',
        'en': 'Hello, {}!\n\nYou can use the bot!'
    }
    get_user = {
        'uz': '<b>Foydalanuvchi buyruqlaridan birini tanlang!</b>',
        'ru': '<b>Выберите одну из команд пользователей!</b>',
        'en': '<b>Choose one of the user commands!</b>'
    }

    settings = {
        'uz': '<b>Sozlamalar menyusidan buyruqlarni tanlang!</b>',
        'ru': '<b>Выберите одну из команд меню настроек!</b>',
        'en': '<b>Choose one of the settings menu commands!</b>'
    }

    change_language = {
        'uz': '<b>Tilni tanlang!</b>',
        'ru': '<b>Выберите язык!</b>',
        'en': '<b>Choose language!</b>'
    }

    add_user = {
        'uz': "<code>O'zgartirmoqchi bo'lgan foydalanuvchini tanlang</code>",
        'ru': "<code>Выберите пользователя, которого хотите изменить</code>",
        'en': "<code>Choose the user you want to change</code>"
    }

    user_already_exists = {
        'uz': '<code>Bu foydalanuvchi allaqachon ro\'yxatdan o\'tgan!</code>',
        'ru': '<code>Этот пользователь уже зарегистрирован!</code>',
        'en': '<code>This user is already registered!</code>'
    }

    user_added = {
        'uz': '<code>Foydalanuvchi ro\'yxatga qo\'shildi!</code>\n\n<b>Qo\'shilgan foydalanuvchi guruhga kiradi</b>',
        'ru': '<code>Пользователь добавлен в список!</code> \n\n<b>Добавленный пользователь войдет в группу</b>',
        'en': '<code>User added to the list!</code> \n\n<b>The added user will enter the group</b>'
    }

    adm_roles = {
        'uz': ["Admin 👮‍♀️", "Kassir 👨🏻‍💻", "Admin va Kassir", "⬅️ Orqaga", "O'chirish 🪓"],
        'ru': ["Админ 👮‍♀️", "Кассир 👨🏻‍💻", "Админ️ и Кассир", "⬅️ Назад", "Удалить 🪓"],
        'en': ["Admin 👮‍♀️", "Cashier 👨🏻‍💻", "Admin and Cashier", "⬅️ Back", "Delete 🪓"]
    }

    roles = {
        'uz': 'Foydalanuvchini qaysi rolga qo\'shmoqchisiz tanlang',
        'ru': 'Выберите, в какую роль добавить пользователя',
        'en': 'Choose which role to add the user'
    }

    change_user = {
        'uz': "{} - foydalanuvchisini qaysi parametrlarini o'zgartirmoqchisiz tanlang",
        'ru': "Выберите, какие параметры пользователя {} хотите изменить",
        'en': "Choose which parameters of user {} you want to change"
    }