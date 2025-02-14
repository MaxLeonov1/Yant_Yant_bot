import json
from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id, Bot, bot
import random
from aiogram import types

@router.message(Command('start_draw'))
async def start_draw(message: Message):
    user_id = message.chat.id
    if user_id in admin_id:
        cursor.execute("SELECT * FROM draw_user_data")
        data = cursor.fetchall()
        random.shuffle(data)
        with open('data/data.json', encoding='utf-8') as file:
            prize = json.loads(file.read())
        text = (f'Розыгрыш завершен \n'
                f'Поздравляем победителей с победой\n')
        for i in range(1):
            text += f'{data[i][1]} - {prize[i]}\n'
        for user in data:
            try:
                await bot.send_message(text=text, chat_id=user[0],reply_markup=types.ReplyKeyboardRemove())
            except:
                pass
        cursor.execute("DELETE FROM draw_user_data")
        con.commit()
        cursor.execute("UPDATE draw_start_reg SET status=(?)", ('False',))
        con.commit()
        return
    await message.answer('Нет доступа')