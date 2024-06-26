from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.database.requests import get_categories, item_category_item, get_basket

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Создать')]

], resize_keyboard=True, one_time_keyboard=True)


create = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать категорию'),
     KeyboardButton(text='Создать товар')]

], resize_keyboard=True, one_time_keyboard=True)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,
                     callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(
        text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def item_by_category(category_id):
    all_items = await item_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(
            text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(
        text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

contacts = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='Инстаграм', url='instagram.com/kirusha_zaidal'), InlineKeyboardButton(text='Телеграм', url='https://t.me/kirushazaidal')]])


add_basket = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='Добавить в корзину', callback_data=f'add_basket'), InlineKeyboardButton(text='На главную', callback_data='to_main')]])

basket = InlineKeyboardMarkup(inline_keyboard=[
                              [InlineKeyboardButton(text='На главную', callback_data='to_main')]])
