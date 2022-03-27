from abc import ABC

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot import database_controller, dp


class HasPermission(BoundFilter):
    key = 'has_permission'

    async def check(self, message: types.Message) -> bool:
        return database_controller.get_status(message.from_user.id)


dp.bind_filter(HasPermission)
