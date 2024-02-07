class Buttom:
    adm_menu = {
        'uz': ["👤 Foydalanuvchilar", "⚙️ Sozlamalar"],
        'ru': ["👤 Пользователи", "⚙️ Настройки"],
        'en': ["👤 Users", "⚙️ Settings"]
    }
    adm_user_menu = {
        'uz': ["✳️ Kiritish", "⛔️ O'chirish", "⬅️ Orqaga"],
        'ru': ["✳️ Добавить", "⛔️ Удалить", "⬅️ Назад"],
        'en': ["✳️ Add", "⛔️ Delete", "⬅️ Back"]
    }
    adm_settings = {
        'uz': ["Tilni o'zgartirish 🌐", "Orqaga ⬅️"],
        'ru': ["Изменить язык 🌐", "Назад ⬅️"],
        'en': ["Change language 🌐", "Back ⬅️"]
    }
    adm_roles = {
        'uz': ["Admin 👮‍♀️", "Kassir 👨🏻‍💻"],
        'ru': ["Админ 👮‍♀️", "Кассир 👨🏻‍💻"],
        'en': ["Admin 👮‍♀️", "Cashier 👨🏻‍💻"]
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
        'uz': "<code>Foydalanuvchi qo'shish uchun u yuborgan xabari yoki uning CHAT_ID sini yuboring</code>",
        'ru': "<code>Для добавления пользователя отправьте сообщение, которое он отправил или его CHAT_ID</code>",
        'en': "<code>To add a user, send the message he sent or his CHAT_ID</code>"
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