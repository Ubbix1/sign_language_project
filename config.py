import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ubbixcode:X3T6Yix71ul9kdmd@cluster0.vntmb.mongodb.net/")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 86400  # 1 day
