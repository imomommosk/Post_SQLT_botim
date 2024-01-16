import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import app
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)

    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer("xush kelibsiz")

    #Adminga xabar yollaymiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qoshildi. \nBazada {count} -ta foydalanuvchi bor"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
