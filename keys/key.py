from aiogram import types

kb_start = [
    types.KeyboardButton(text='Регистрация'),
    types.KeyboardButton(text='Информация'),
    types.KeyboardButton(text='Команды')
]
kb_command = [
    types.KeyboardButton(text='/start_reg'),
    types.KeyboardButton(text='/end_reg'),
    types.KeyboardButton(text='/start_draw'),
]