from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from data_module import get_name

# начальная клавиатура
start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

# клавиатура меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Список заместителей")],
        [KeyboardButton(text="Просмотреть информацию о заместителях")],
        [KeyboardButton(text="Выйти из меню")]
    ],
    resize_keyboard=True
)


# функция для создания inline-клавиатуры с заместителями
def get_dep_inl():
    deputies = get_name()
    keyboard = []
    if deputies:
        for dep in deputies:
            keyboard.append([InlineKeyboardButton(text=dep[0], callback_data=f"dep_{dep[0]}")])
    else:
        keyboard.append([InlineKeyboardButton(text="Нет заместителей")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# функция для создания inline-клавиатуры для конкретного заместителя
def get_dep_opt(name):
    keyboard = [
        [
            InlineKeyboardButton(text="Совещание", callback_data=f"meet_{name}"),
            InlineKeyboardButton(text="Назначить задачу", callback_data=f"task_{name}")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
