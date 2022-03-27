from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot import database_controller, dp


class UserSaverMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        # if update has a message, not a callback query
        if not update.message:
            return

        user_id = update.message.from_user.id

        if not database_controller.is_user_exists(user_id):
            user_data = {
                'id': update.message.from_user.id,
                'first_name': update.message.from_user.first_name,
                'last_name': update.message.from_user.last_name,
                'username': update.message.from_user.username
            }
            database_controller.add_user(user_data)


dp.setup_middleware(UserSaverMiddleware())
