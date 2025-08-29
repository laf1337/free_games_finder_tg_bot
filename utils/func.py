import asyncio
from parser.pars import sale_massage_parser
from database.db import Database
from database.shared import latest_data
from aiogram import Bot

db = Database("users_data.db")

async def sendgameslist(bot: Bot):
    users = await db.get_subscribed_ids()
    message_text = latest_data
    for user_id in users:
        try:
            await bot.send_message(user_id, message_text)
        except Exception:
            print(f"Can't send message {user_id}")
            await db.remove_user(user_id)
             
async def parser_loop():
    print("[i] Wait new data...")
    loop = asyncio.get_running_loop()
    while True:
        latest_data = await loop.run_in_executor(None, sale_massage_parser)
        print("[i] Data updated!")
        await asyncio.sleep(43200)

async def daily_broadcast(bot: Bot):
    while True:
        print("[i] 24h to next mail")
        await asyncio.sleep(86400)
        print("[i] mail started")
        sendgameslist(bot)

async def tasks_on_startup(bot: Bot):
    await db.createdb()
    asyncio.create_task(parser_loop())
    asyncio.create_task(daily_broadcast(bot))
    print("[i] Startup task created")

