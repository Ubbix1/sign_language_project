from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user_model import User

class AuthService:
    @staticmethod
    async def register_user(name, email, password, role="customer"):
        """Registers a new user with hashed password"""
        existing_user = await User.find_by_email(email)
        if existing_user:
            return {"error": "User already exists"}, 400

        hashed_password = generate_password_hash(password)
        await User.create_user(name, email, hashed_password, role)
        return {"message": "User registered successfully"}, 201

    @staticmethod
    async def login_user(email, password):
        """Authenticates user and generates JWT tokens"""
        is_valid = await User.verify_password(email, password)
        if not is_valid:
            return {"error": "Invalid email or password"}, 401

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200
