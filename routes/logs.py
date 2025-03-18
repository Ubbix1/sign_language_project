from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.log_model import Log
import asyncio

logs_bp = Blueprint("logs_bp", __name__)

@logs_bp.route("/logs", methods=["GET"])
@jwt_required()
async def get_logs():
    """Fetches all logs (Admin Only)"""
    user_email = get_jwt_identity()
    user_role = await Log.get_user_role(user_email)

    if user_role != "admin":
        return jsonify({"error": "Unauthorized access"}), 403

    logs = await Log.get_all_logs()
    return jsonify({"logs": logs}), 200

@logs_bp.route("/logs", methods=["POST"])
@jwt_required()
async def add_log():
    """Stores logs for user activities, security, and predictions"""
    data = await request.get_json()
    user_email = get_jwt_identity()

    log_data = {
        "user": user_email,
        "activity": data.get("activity", "Unknown"),
        "details": data.get("details", ""),
    }

    await Log.create_log(log_data)
    return jsonify({"message": "Log entry added"}), 201
