from aiogram.types import Message
from loader import router, cursor, con
from aiogram import F

@router.message(F.text == 'Информация')
async def info_req(message:Message):
    with open('info.txt',encoding='utf-8') as info:
        info_ = str(info.read())
        await message.answer(text = info_)
