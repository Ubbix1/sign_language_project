from motor.motor_asyncio import AsyncIOMotorClient
import os

class Database:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:5000")  # Use Render's env variable
    DATABASE_NAME = os.getenv("DATABASE_NAME", "sign_language_db")  # Default DB name

    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]  # Correctly set the database instance
