from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id
from aiogram import types

@router.message(Command('end_reg'))
async def adm_start_reg(message: Message):
    user_id = message.chat.id
    if user_id in admin_id:
        cursor.execute("UPDATE draw_start_reg SET status=(?)",('False',))
        con.commit()
        await message.answer('Регистрация завершена',reply_markup=types.ReplyKeyboardRemove())
        return
    await message.answer('Нет доступа')
