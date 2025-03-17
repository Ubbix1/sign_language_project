from database import mongo
from datetime import datetime

class Prediction:
    @staticmethod
    def save_prediction(user_id, predicted_sign, confidence):
        return mongo.db.predictions.insert_one({
            "user_id": user_id,
            "predicted_sign": predicted_sign,
            "confidence": confidence,
            "timestamp": datetime.utcnow()
        })
