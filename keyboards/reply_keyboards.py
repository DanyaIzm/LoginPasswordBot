from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть пароль")],
    [KeyboardButton(text="Посмотреть все логины и пароли"), KeyboardButton(text="Добавить новый аккаунт")],
    [KeyboardButton(text="Удалить аккаунт"), KeyboardButton(text="Изменить пароль")]
],
                                         resize_keyboard=True)
