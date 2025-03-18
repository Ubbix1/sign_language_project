from motor.motor_asyncio import AsyncIOMotorClient
import os

# Load database URL from environment variables or use a default
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ubbixcode:X3T6Yix71ul9kdmd@cluster0.vntmb.mongodb.net/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "sign_language_db")  # Set default DB name

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]  # Now explicitly specifying a database

class Database:
    """MongoDB database connection"""
    @staticmethod
    def get_db():
        return db
