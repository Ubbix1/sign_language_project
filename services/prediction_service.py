import tensorflow as tf
import numpy as np
from PIL import Image
from models.prediction_model import Prediction

class PredictionService:
    model = tf.lite.Interpreter(model_path="sign_language_model.tflite")
    model.allocate_tensors()
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    @staticmethod
    def preprocess_image(image):
        """Prepares image for AI model"""
        image = image.resize((96, 96)).convert("RGB")  # Resize & Convert
        image = np.array(image, dtype=np.float32) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    @staticmethod
    async def predict_sign_language(image):
        """Processes image and returns predicted sign"""
        processed_img = PredictionService.preprocess_image(image)
        PredictionService.model.set_tensor(PredictionService.input_details[0]["index"], processed_img)
        PredictionService.model.invoke()
        prediction = PredictionService.model.get_tensor(PredictionService.output_details[0]["index"])

        predicted_sign = chr(np.argmax(prediction) + 65)  # Convert index to A-Z
        confidence = float(np.max(prediction))

        return {"sign": predicted_sign, "confidence": confidence}

    @staticmethod
    async def save_prediction(user_id, predicted_sign, confidence):
        """Stores AI prediction results in MongoDB"""
        await Prediction.save_prediction(user_id, predicted_sign, confidence)
