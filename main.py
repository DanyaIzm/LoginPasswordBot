import logging
from aiogram import executor

# importing dispatcher from the bots file
from bot import dp

# importing all needed stuff
import handlers

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=False)