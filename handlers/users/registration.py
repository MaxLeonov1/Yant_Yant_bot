from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, cursor, con
from aiogram import F

class Form_reg(StatesGroup):
    fio = State()
    phone = State()
    email = State()
    age = State()

@router.message(F.text == 'Регистрация')
async def start_reg(message: Message, state: FSMContext):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM draw_user_data WHERE id=(?)",(user_id,))
    if len(cursor.fetchall())>0:
        await message.answer(text='Вы уже зарегистрированы')
        return
    cursor.execute("SELECT status FROM draw_start_reg")
    if cursor.fetchall() == 'False':
        await message.answer(text='Регистрация уже завершена')
        return
    await state.set_state((Form_reg.fio))
    await message.answer('Для начала введите ФИО полностью',reply_markup=types.ReplyKeyboardRemove())

############Регистрация##################

@router.message(Form_reg.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await state.set_state(Form_reg.age)
    await message.answer('Введи свой возраст')

@router.message(Form_reg.age)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form_reg.phone)
    await message.answer('Введи номер телефона')

@router.message(Form_reg.phone)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Form_reg.email)
    await message.answer('Введи свой email')

@router.message(Form_reg.email)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    fio = data['fio']
    age = data['age']
    phone = data['phone']
    email = data['email']
    user_id = message.chat.id
    await state.clear()
    cursor.execute("INSERT INTO draw_user_data (id,FIO,phone,email,age) VALUES (?,?,?,?,?)",
                   (user_id,fio,phone,email,age))
    con.commit()
    await message.answer('Регистрация завершена')

###############################################################

