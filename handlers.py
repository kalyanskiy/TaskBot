import data_module as dm
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from kb import start, menu, get_dep_inl, get_dep_opt

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
        res = "\n\n".join([f"Telegram ID: {dep[0]}\nФИО: {dep[1]}\nДата рождения: {dep[2]}\nЧин:"
                           f" {dep[3]}\nОтдел: {dep[4]}\nТелефон: {dep[5]}\nПочта: {dep[6]}" for dep in deputies])
    else:
        res = "Нет информации"
    await message.answer(res)


@router.message(F.text.lower() == "список заместителей")
async def list_deputies(message: Message):
    await message.answer("Выберите заместителя:", reply_markup=get_dep_inl())


@router.message(F.text.lower() == "выйти из меню")
async def exit_menu(message: Message):
    await message.answer("Вы вышли из меню", reply_markup=start)


@router.callback_query(F.data.startswith("dep_"))
async def choose_dep(callback: CallbackQuery):
    name = callback.data[len("dep_"):]
    await callback.message.answer(f"Выбран(а) зам. министр: {name}", reply_markup=get_dep_opt(name))
    await callback.answer()


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer("Выберите заместителя:", reply_markup=get_dep_inl())
    await callback.answer()
