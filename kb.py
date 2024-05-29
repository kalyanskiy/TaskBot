from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Просмотреть информацию о заместителях")],
        [KeyboardButton(text="Выйти из меню")]
    ],
    resize_keyboard=True
)
