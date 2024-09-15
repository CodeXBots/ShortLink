from motor.motor_asyncio import AsyncIOMotorClient
from configs import *

class Database:

    def __init__(self, url, db_name):
        self.db = AsyncIOMotorClient(url)[db_name]
        self.coll = self.db.users

    async def add_user(self, id):
        if not await self.is_present(id):
            await self.coll.insert_one(dict(id=id, api=None, shortner=None))

    async def is_present(self, id):
        return bool(await self.coll.find_one({'id': int(id)}))

    async def total_users(self):
        return await self.coll.count_documents({})

    async def set_shortner(self, uid, shortner, api):
        await self.coll.update_one({'id': uid}, {'$set': {'shortner': shortner, 'api': api}})

    async def get_value(self, key, uid):
        user = await self.coll.find_one({'id': uid})
        return user.get(key, None)


db = Database(DATABASE_URL, "CodeXBots")
