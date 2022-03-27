from aiogram import types

from bot import dp


@dp.message_handler()
async def echo_message(message: types.Message):
    await dp.bot.send_message(chat_id=message.chat.id, text=f"{message.text}")
