from flask import Blueprint, jsonify
from database import mongo

log_bp = Blueprint("log_bp", __name__)

@log_bp.route("/logs", methods=["GET"])
def get_logs():
    logs = list(mongo.db.logs.find({}, {"_id": 0}))
    return jsonify(logs), 200
