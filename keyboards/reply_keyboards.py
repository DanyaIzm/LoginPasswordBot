from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть все логины и пароли")],
    [KeyboardButton(text="Посмотреть пароль"), KeyboardButton(text="Добавить новый аккаунт")]
],
                                         resize_keyboard=True)
