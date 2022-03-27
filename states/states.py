from aiogram.dispatcher.filters.state import StatesGroup, State


class GetPasswordStatesGroup(StatesGroup):
    get_service = State()


class DeleteAccountStatesGroup(StatesGroup):
    get_service_and_login = State()


class ChangePasswordStatesGroup(StatesGroup):
    get_service_and_login = State()
    get_new_password = State()


class AddNewAccountStatesGroup(StatesGroup):
    get_service_name = State()
    get_login = State()
    get_password = State()
