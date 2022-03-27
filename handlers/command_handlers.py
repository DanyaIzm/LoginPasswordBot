from aiogram import types

from bot import dp

# Keyboards
from keyboards import *


@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    await message.reply("Привет, я бот-помощник Password_Saver_3000.\n"
                        "Я помогу тебе сохранить твои логины и пароли, чтобы ты их не забыл(а)!\n=3",
                        reply_markup=main_menu_keyboard)


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.reply("Эх, я бы с радостью тебе помог, "
                        "но на данном этапе я ещё в разработке, и поэтому сам не знаю, "
                        "что умею и буду уметь делать, хех...")


@dp.message_handler(commands=['menu'])
async def menu_message(message: types.Message):
    await message.reply("Открываю главное меню",
                        reply_markup=main_menu_keyboard)