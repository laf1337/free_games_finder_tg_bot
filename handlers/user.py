from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from database.db import Database
from keyboards import reply, inline
from database.shared import latest_data
db = Database("users_data.db")
router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await db.add_user(message.from_user.id)
    await message.answer(f"Выберите действие из меню", reply_markup=reply.main)

@router.message(Command("id"))
async def sendid(message: Message):
    await message.answer(str(message.from_user.id))

@router.message(Command("sub"))
@router.message(F.text.lower() == "подписаться на рассылку")
async def sub(message: Message):
    user_id = message.from_user.id
    await db.add_user(user_id=user_id)
    await db.set_subscribed(user_id, 1)
    await message.answer(f"Вы успешно подписанны на рассылку!")

@router.message(Command("unsub"))
@router.message(F.text.lower() == "отписаться от рассылки")
async def sub(message: Message):
    user_id = message.from_user.id
    await db.set_subscribed(user_id, 0)
    await message.answer(f"Вы отписались от расслыки!")

@router.message(Command("freegames"))
@router.message(F.text.lower() == "получить список бесплатных игр")
async def sub(message: Message):
    await message.answer(latest_data, reply_markup=inline.links)