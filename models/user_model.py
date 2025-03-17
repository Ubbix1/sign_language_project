from database import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    collection = Database.db.users

    @staticmethod
    async def create_user(name, email, password, role="customer"):
        hashed_pw = generate_password_hash(password)
        await User.collection.insert_one({
            "name": name,
            "email": email,
            "password": hashed_pw,
            "role": role
        })

    @staticmethod
    async def find_by_email(email):
        return await User.collection.find_one({"email": email})

    @staticmethod
    async def verify_password(email, password):
        user = await User.find_by_email(email)
        return user and check_password_hash(user["password"], password)
