from aiogram import types

from bot import dp, database_controller

# Filters
from filters.permission_filter import HasPermission


@dp.message_handler(HasPermission(), text="Посмотреть все логины и пароли")
async def get_accounts_message(message: types.Message):
    data = database_controller.get_from_accounts('everything', message.from_user.id)
    if not data:
        await dp.bot.send_message(chat_id=message.chat.id, text="Вы ещё не добавили аккаунты сюда")
        return

    text = "Вот все аккаунты: \n"

    for item in data:
        item_text = f"\n🛠: {item['service']}\n" \
                    f"👤: {item['login']}\n" \
                    f"🔑: {item['password']}"
        text = text + item_text + "\n"

    await dp.bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(HasPermission(), text="Посмотреть пароль")
async def get_account_by_service_message(message: types.Message):
    pass


@dp.message_handler(HasPermission(), text="Добавить новый аккаунт")
async def add_account_message(message: types.Message):
    pass


@dp.message_handler(HasPermission(), text="Удалить аккаунт")
async def delete_account_message(message: types.Message):
    pass


@dp.message_handler(HasPermission(), text="Изменить пароль")
async def change_password_message(message: types.Message):
    pass


@dp.message_handler()
async def unknown_message(message: types.Message):
    await dp.bot.send_message(chat_id=message.chat.id, text=f"Я вас не понимаю :(")
