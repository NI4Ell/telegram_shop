from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

class User_message(StatesGroup):
    message = State()

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Привет, {message.from_user.full_name}! Добро пожаловать в магазин!')

@router.message(Command('shop'))
async def shop(message: Message):
    await message.answer('Что вам нужно?',reply_markup= kb.start)

@router.message(F.text == 'Создать категорию')
async def create_category(message: Message, state: FSMContext):
    await message.answer('Напишите название категории')
    await state.set_state(User_message.message)

@router.message(User_message.message)
async def create_category_final(message: Message, state: FSMContext):
    await state.update_data(message = message.text)
    data = await state.get_data()
    await rq.set_category(data["message"])
    await state.clear()
    
    

