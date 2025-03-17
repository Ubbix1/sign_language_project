from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user_model import User
import asyncio

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
async def register():
    data = await request.get_json()
    existing_user = await User.find_by_email(data["email"])
    
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    await User.create_user(data["name"], data["email"], data["password"])
    return jsonify({"message": "User registered successfully"}), 201

@user_bp.route("/login", methods=["POST"])
async def login():
    data = await request.get_json()
    is_valid = await User.verify_password(data["email"], data["password"])

    if not is_valid:
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=data["email"])
    refresh_token = create_refresh_token(identity=data["email"])

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
