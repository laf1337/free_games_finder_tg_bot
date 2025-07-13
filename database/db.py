import aiosqlite as sq

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def createdb(self):
        async with sq.connect(self.db_path) as data:
            await data.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    subscribed INTEGER NOT NULL DEFAULT 0,
                    is_admin INTEGER NOT NULL DEFAULT 0
                    )""")
            await data.commit()

    async def add_user(self, user_id: int):
        async with sq.connect(self.db_path) as data:
            await data.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
            await data.commit()
            print(f"Done! Tg id: {user_id}")

    async def remove_user(self, user_id: int):
        async with sq.connect(self.db_path) as data:
            await data.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            await data.commit()
            print("Done!")

    async def set_subscribed(self, user_id: int, is_sub: int):
        async with sq.connect(self.db_path) as data:
            await data.execute("UPDATE users SET subscribed = ? WHERE user_id = ?", (is_sub, user_id,))
            await data.commit()

    async def promote_to_admin(self, user_id: int):
        async with sq.connect(self.db_path) as data:
            await data.execute("UPDATE users SET is_admin = 1 WHERE user_id = ?", (user_id,))
            await data.commit()

    async def is_admin(self, user_id: int):
        async with sq.connect(self.db_path) as data:
            async with data.execute("SELECT is_admin FROM users WHERE user_id = ?", (user_id,)) as cur:
                result = await cur.fetchone()
                return result is not None and result[0] == 1
    
    async def get_subscribed_ids(self):
        async with sq.connect(self.db_path) as data:
            async with data.execute("SELECT user_id FROM users WHERE subscribed = 1") as cur:
                result = [row[0] for row in await cur.fetchall()]
                return result

# while True:
#     a = int(input("Нажмите 1 чтобы добавить ползователя"))
#     if a == 1:
#         userid = int(input("Введите id"))
#         add_user_db(userid)
#     elif a == 2:
#         userid = int(input("Введите id"))
#         remove_user_db(userid)
#     elif a == 3:
#         userid = int(input("Введите id"))
#         sub = int(input("Введите 1 0"))
#         user_sub(user_id=userid, is_sub=sub)
#     elif a == 4:
#         userid = int(input("Введите id"))
#         op_user(userid)
#     elif a == 5:
#         userid = int(input("Введите id"))
#         if has_permited(userid):
#             print("С админкой!!")
#         else:
#             print("Без админки!")
#     elif a == 6:
#         print(subscribed_ids())
#     else:
#         break
