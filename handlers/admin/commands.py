from aiogram.types import Message
from loader import router, cursor, con, admin_id
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_command

@router.message(F.text == 'Команды')
async def adm_commands(message: Message):
    user_id = message.chat.id
    if user_id in admin_id:
        builder = ReplyKeyboardBuilder()
        for button in kb_command:
            builder.add(button)
        builder.adjust(1)
        await message.answer(text='Список команд', reply_markup=builder.as_markup(resize_keyboard=True))
        return
    await message.answer('Нет доступа')