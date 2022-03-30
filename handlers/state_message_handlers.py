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


# DeleteAccount
@dp.message_handler(HasPermission(), text="Удалить аккаунт")
async def get_service_and_login_to_delete_message(message: types.Message):
    await DeleteAccountStatesGroup.get_service_and_login.set()
    await message.reply("Введите название сервиса и логин (через пробел), "
                        "и я удалю ваш аккаунт НАВСЕГДА (нет, хех... Или да :>)")


@dp.message_handler(HasPermission(), state=DeleteAccountStatesGroup.get_service_and_login)
async def delete_account_and_reply_message(message: types.Message, state: FSMContext):
    try:
        text = message.text.split(" ")
        service = text[0]
        login = None

        if len(text) >= 2:
            login = text[1]

        amount_of_records = database_controller.delete_account(message.from_user.id, service, login)

        if amount_of_records == 0:
            await dp.bot.send_message(chat_id=message.from_user.id, text="Таких записей нет, увы :<")
        else:
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text=f"Ура, удалось удалить {amount_of_records} записей")

    except Exception as e:
        await dp.bot.send_message(chat_id=message.from_user.id, text="Не удалось удалить аккаунт \n:__(")
    finally:
        await state.finish()


# Change password
@dp.message_handler(HasPermission(), text="Изменить пароль")
async def change_password_message(message: types.Message):
    await ChangePasswordStatesGroup.get_service_and_login.set()
    await message.reply("Отлично. Введите название сервиса и логин (через пробел).\n"
                        "Если у вас только один аккаунт на сервисе, то можно и без логина :>")


@dp.message_handler(HasPermission(), state=ChangePasswordStatesGroup.get_service_and_login)
async def get_login_and_service_to_change_password_message(message: types.Message, state: FSMContext):
    try:
        text = message.text.split(" ")
        service = text[0]
        login = None

        if len(text) >= 2:
            login = text[1]

        amount_of_records = database_controller.get_accounts_amount(message.from_user.id, service)

        if amount_of_records > 1 and not login:
            await dp.bot.send_message(chat_id=message.from_user.id, text="Пожалуйста, пришлите логин тоже.\n"
                                                                         "У вас несколько записей в БД :<")
            # Try again
            return

        if amount_of_records == 0:
            await dp.bot.send_message(chat_id=message.from_user.id, text="Таких записей нет, увы :<")
            return await state.finish()
        else:
            # Save service and login into the storage
            await state.set_data({
                "service": service,
                "login": login
            })

            await dp.bot.send_message(chat_id=message.from_user.id, text=f"Теперь введите новый пароль c:")
            # Go to the next state
            await ChangePasswordStatesGroup.get_new_password.set()

    except Exception as e:
        await dp.bot.send_message(chat_id=message.from_user.id, text="Не удалось найти записи \n:__(")
        return await state.finish()


@dp.message_handler(HasPermission(), state=ChangePasswordStatesGroup.get_new_password)
async def get_new_password_and_change_it_message(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        database_controller.change_password(user_id=message.from_user.id, new_password=message.text,
                                            service=data["service"], login=data["login"])

        await dp.bot.send_message(chat_id=message.from_user.id, text="Пароль был успешно изменён! :>")

    except Exception as e:
        await dp.bot.send_message(chat_id=message.from_user.id, text="Не удалось изменить пароль\n:__(")
    finally:
        return await state.finish()
