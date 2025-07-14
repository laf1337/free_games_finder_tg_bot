from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.db import Database
from parser.pars import sale_massage_parser
from utils.func import sendgameslist
db = Database("users_data.db")
router = Router()

@router.message(Command("test"))
async def test(message:Message):
    if await db.is_admin(message.from_user.id):
        await message.answer(f"Подготовка списка игр для вас! <b> Ожидайте 3-5 минут </b>")
        await message.answer(str(sale_massage_parser()))
    else:
        await message.answer(f"Недостаточно прав")

@router.message(Command("sendgamestoall"))
async def sendall(message:Message):
    if await db.is_admin(message.from_user.id):
        await message.answer(f"Успешно")
        sendgameslist(message.bot)
    else:
        await message.answer(f"Недостаточно прав")