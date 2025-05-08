import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router as start

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Routerni ro'yxatga olamiz
    dp.include_router(start)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
