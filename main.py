import logging
from aiogram import Bot, Dispatcher, executor

from config.config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

# Creating a bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=False)