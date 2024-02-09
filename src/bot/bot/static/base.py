class Button:
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


class KButtons:
    manu = {
        'uz': ["🔢 Kalonka ko'rsatkichi", "💰 Bugungi savdo", "⚙️ Sozlamalar"],
        'ru': ["🔢 Кассовый аппарат", "💰 Текущая продажа", "⚙️ Настройки"],
        'en': ["🔢 Cash register", "💰 Current sale", "⚙️ Settings"]
    }

    fuel_columns = {
        'uz': ["🕑 Kun boshiga", "Kun oxiriga 🕘", "⬅️ Orqaga"],
        'ru': ["🕑 На начало дня", "На конец дня 🕘", "⬅️ Назад"],
        'en': ["🕑 At the beginning of the day", "At the end of the day 🕘", "⬅️ Back"]
    }


class KTexts:
    start = {
        'uz': 'Assalom alaykum, {}!\n\nBotdan foydalanishingiz mumkin!',
        'ru': 'Здравствуйте, {}!\n\nВы можете использовать бота!',
        'en': 'Hello, {}!\n\nYou can use the bot!'
    }
    fuel_column = {
        'uz': "<b>Qaysi kalonka ko'rsatgichini tanlamoqchisiz?</b>",
        'ru': "<b>Какой колонки вы хотите выбрать?</b>",
        'en': "<b>Which fuel column do you want to choose?</b>"
    }
    column_chosen = {
        'uz': "<b>Siz <code>{}</code> yoqilg'i uchun <code> {} </code> kalonkasini tanladingiz!\n\nKalonka ko'rsatgichini qaysi vaqt uchun kiritmoqchisiz tanlang va kiriting</b>",
        'ru': "<b>Вы выбрали колонку <code> {} </code> для топлива <code>{}</code>!\n\nВыберите и введите время для колонки</b>",
        'en': "<b>You have chosen column <code> {} </code> for fuel <code>{}</code>!\n\nChoose and enter the time for the column</b>"
    }
    fuel_column_numbers = {
        'uz': "Kalonka ko'rsatgichini kiriting",
        'ru': "Введите номер колонки",
        'en': "Enter the column number"
    }

    fuel_type = {
        'uz': "<b>Qaysi turdagi yoqilg'i uchun kiritmoqchisiz tanlang</b>",
        'ru': "<b>Выберите, для какого типа топлива вы хотите ввести данные</b>",
        'en': "<b>Choose for which type of fuel you want to enter data</b>"
    }

    fuel_type_chosen = {
        'uz': "<b>Siz <code> {} </code> turdagi yoqilg'i uchun tanladingiz!</b>",
        'ru': "<b>Вы выбрали топливо для типа <code> {} </code>!</b>",
        'en': "<b>You have chosen fuel for the type <code> {} </code>!</b>"
    }
    column_num_already_exist_1 = {
        'uz': "<b>Bu vaqt uchun bu raqamli kalonka allaqachon kiritilgan!\n\nKun boshidagi ko'rsatgich: {}</b>",
        'ru': "<b>Этот номер колонки уже введен для этого времени!\n\nКолонка на начало дня: {}</b>",
        'en': "<b>This column number has already been entered for this time!\n\nColumn at the beginning of the day: {}</b>"
    }
    column_num_already_exist_2 = {
        'uz': "<b>Bu vaqt uchun bu raqamli kalonka allaqachon kiritilgan!\n\nKun oxiridagi ko'rsatgich: {}</b>",
        'ru': "<b>Этот номер колонки уже введен для этого времени!\n\nКолонка на конец дня: {}</b>",
        'en': "<b>This column number has already been entered for this time!\n\nColumn at the end of the day: {}</b>"
    }
    column_num_success = {
        'uz': "<b>Kalonka raqami muvaffaqiyatli kiritildi!</b>",
        'ru': "<b>Номер колонки успешно введен!</b>",
        'en': "<b>Column number entered successfully!</b>"
    }

    column_num_error = {
        'uz': "<b>Kalonka raqami raqam bo'lishi kerak!</b>",
        'ru': "<b>Номер колонки должен быть числом!</b>",
        'en': "<b>Column number must be a number!</b>"
    }
