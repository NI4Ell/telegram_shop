from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq


router = Router()


class User_message(StatesGroup):
    message = State()


class Creat_item(StatesGroup):
    name = State()
    discr = State()
    price = State()
    category = State()


@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Привет, {message.from_user.full_name}! Добро пожаловать в магазин!')


@router.message(Command('shop'))
async def shop(message: Message):
    await message.answer('Что вам нужно?', reply_markup=kb.start)


@router.message(F.text == 'Создать')
async def create(message: Message):
    await message.answer('Что вы хотите создать?', reply_markup=kb.create)


@router.message(F.text == 'Создать категорию')
async def create_category(message: Message, state: FSMContext):
    await message.answer('Напишите название категории')
    await state.set_state(User_message.message)


@router.message(User_message.message)
async def create_category_final(message: Message, state: FSMContext):
    await state.update_data(message=message.text)
    data = await state.get_data()
    await rq.set_category(data["message"])
    await message.answer('Спасибо за создание категории')
    await state.clear()


@router.message(F.text == 'Создать товар')
async def create_item(message: Message, state: FSMContext):
    await message.answer('Напишите название товара')
    await state.set_state(Creat_item.name)


@router.message(Creat_item.name)
async def create_name_item(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Creat_item.discr)
    await message.answer('Напишите описание товара')


@router.message(Creat_item.discr)
async def create_discr_item(message: Message, state: FSMContext):
    await state.set_state(User_message.message)
    await state.update_data(discr=message.text)
    await state.set_state(Creat_item.price)
    await message.answer('Напишите цену товара')


@router.message(Creat_item.price)
async def create_discr_2(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Creat_item.category)
    await message.answer('Напишите категорию предмета')


@router.message(Creat_item.category)
async def create_item_final(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()
    await message.answer('Спасибо за создание товара')
    await rq.set_item(data["name"], data["discr"], data["price"], data["category"])
    await state.clear()


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберете категорию товара', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберете товар по категории', reply_markup=await kb.item_by_category(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('')
    await callback.message.answer(f'Вы выбрали товар: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')
