from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

class Database:
    client = AsyncIOMotorClient(Config.MONGO_URI)
    db = client.get_database()
