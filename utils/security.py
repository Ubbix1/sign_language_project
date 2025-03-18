from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
import re
from datetime import timedelta

class Security:
    """Handles authentication and security utilities"""

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password securely"""
        return generate_password_hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verifies if a password matches its hashed version"""
        return check_password_hash(hashed_password, password)

    @staticmethod
    def create_tokens(email: str):
        """Generates access and refresh tokens for a user"""
        access_token = create_access_token(identity=email, expires_delta=timedelta(hours=2))
        refresh_token = create_refresh_token(identity=email, expires_delta=timedelta(days=7))
        return {"access_token": access_token, "refresh_token": refresh_token}

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates an email format"""
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(regex, email) is not None

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        Validates password strength:
        - At least 8 characters
        - At least 1 uppercase letter
        - At least 1 lowercase letter
        - At least 1 digit
        - At least 1 special character
        """
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return re.match(regex, password) is not None

    @staticmethod
    def decode_jwt(token: str):
        """Decodes a JWT token without verifying its signature"""
        try:
            return decode_token(token)
        except Exception as e:
            return {"error": str(e)}
