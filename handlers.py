import data_module as dm
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from kb import start, menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=start)


@router.message(F.text.lower() == "меню")
async def cmd_menu(message: Message):
    await message.answer("Вы вошли в меню", reply_markup=menu)


@router.message(F.text.lower() == "просмотреть информацию о заместителях")
async def view_deputies(message: Message):
    deputies = dm.get_deputies()
    if deputies:
        res = "\n\n".join([f"Telegram ID: {dep[0]}\nName: {dep[1]}\nBirthday: {dep[2]}\nPosition:"
                           f" {dep[3]}\nDepartment: {dep[4]}\nPhone: {dep[5]}\nEmail: {dep[6]}" for dep in deputies])
    else:
        res = "Нет информации"
    await message.answer(res)


@router.message(F.text.lower() == "выйти из меню")
async def exit_menu(message: Message):
    await message.answer("Вы вышли из меню", reply_markup=start)
