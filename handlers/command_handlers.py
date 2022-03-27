from aiogram import types

from bot import dp


@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    await message.reply("Привет, я бот-помощник Password_Saver_3000.\n"
                        "Я помогу тебе сохранить твои логины и пароли, чтобы ты их не забыл(а)!\n=3")


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.reply("Эх, я бы с радостью тебе помог, "
                        "но на данном этапе я ещё в разработке, и поэтому сам не знаю, "
                        "что умею и буду уметь делать, хех...")
