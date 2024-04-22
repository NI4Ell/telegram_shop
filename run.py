import os
from aiogram import Dispatcher, Bot
import logging
import asyncio
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main
from bot import bot


dp = Dispatcher()


async def main():
    await async_main()
    load_dotenv()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
