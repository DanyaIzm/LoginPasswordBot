from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp, database_controller

# Filters
from filters.permission_filter import HasPermission

# States
from states import *


# GetPassword
@dp.message_handler(HasPermission(), text="Посмотреть пароль")
async def get_password_message(message: types.Message):
    await GetPasswordStatesGroup.get_service.set()
    await message.reply("Отлично. Введите название сервиса, и я пришлю вам пароль")


@dp.message_handler(HasPermission(), state=GetPasswordStatesGroup.get_service)
async def reply_with_a_password_message(message: types.Message, state: FSMContext):
    try:
        data = database_controller.get_from_accounts("service", message.from_user.id, message.text)

        if not data:
            await dp.bot.send_message(chat_id=message.chat.id, text="Увы, таких акканутов у меня в базе данных нет :O")
            return await state.finish()

        text = "Вот все аккаунты: \n"

        for item in data:
            item_text = f"\n🛠: {item['service']}\n" \
                        f"👤: {item['login']}\n" \
                        f"🔑: {item['password']}"
            text = text + item_text + "\n"

        await dp.bot.send_message(chat_id=message.chat.id, text=text)

    except Exception as e:
        await dp.bot.send_message(chat_id=message.from_user.id, text="Не удалось получить данные :(")
    finally:
        await state.finish()
