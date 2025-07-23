import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import Router

BOT_TOKEN = "7707365462:AAE9eE_P1p0BZBLs91-8fuJJyYAWiP_h3Rg"

async def main():
    bot = Bot( BOT_TOKEN )
    dp = Dispatcher()
    dp.include_router( Router )

    await dp.start_polling( bot )

if __name__ == "__main__":
    asyncio.run( main() )