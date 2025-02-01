from motor.motor_asyncio import AsyncIOMotorClient

from data.config import MONGO_NAME, MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_NAME]

users_collection = db["users"]
