from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id

@router.message(Command('start_reg'))
async def adm_start_reg(message: Message):
    user_id = message.chat.id
    if user_id in admin_id:
        cursor.execute("UPDATE draw_start_reg SET status=(?)",('True',))
        con.commit()
        await message.answer('Регистрация запущена')
        return
    await message.answer('Нет доступа')
