from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN

from database import DatabaseController

# Creating a bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Creating a database controllet instance
database_controller = DatabaseController()