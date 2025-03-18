from database import db

class User:
    collection = db["users"]  # Users collection

    @staticmethod
    async def find_by_username(username):
        """Find a user by username"""
        return await User.collection.find_one({"username": username})

    @staticmethod
    async def create_user(user_data):
        """Insert a new user into the database"""
        return await User.collection.insert_one(user_data)

    @staticmethod
    async def update_user(username, update_data):
        """Update user details"""
        return await User.collection.update_one(
            {"username": username}, {"$set": update_data}
        )

    @staticmethod
    async def delete_user(username):
        """Delete a user by username"""
        return await User.collection.delete_one({"username": username})


class Prediction:
    collection = db["predictions"]  # Predictions collection

    @staticmethod
    async def store_prediction(user_id, prediction_data):
        """Store a prediction result for a user"""
        prediction = {
            "user_id": user_id,
            "prediction": prediction_data,
        }
        return await Prediction.collection.insert_one(prediction)

    @staticmethod
    async def get_predictions_by_user(user_id):
        """Get all predictions made by a user"""
        return await Prediction.collection.find({"user_id": user_id}).to_list(length=100)
