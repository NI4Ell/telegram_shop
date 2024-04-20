from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Создать')]

], resize_keyboard= True)


create = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать категорию'), KeyboardButton(text='Создать товар')]

], resize_keyboard= True)

