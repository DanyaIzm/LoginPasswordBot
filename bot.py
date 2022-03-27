from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config.config import BOT_TOKEN

from database import DatabaseController

# Creating a storage
storage = MemoryStorage()

# Creating a bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

# Creating a database controllet instance
database_controller = DatabaseController()
