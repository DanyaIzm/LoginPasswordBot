from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN

# Creating a bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
