import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import get_token
from utils.func import tasks_on_startup
from handlers import admin, fallback, user


async def main():
    bot = Bot(token=get_token(), default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    
    dp.include_routers(
        user.router,
        admin.router,
        fallback.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await tasks_on_startup(bot)
    print("[I] Bot online")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())