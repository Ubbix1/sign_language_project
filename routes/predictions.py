from flask import Blueprint, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
from models.prediction_model import Prediction

prediction_bp = Blueprint("prediction_bp", __name__)

# Load TensorFlow Model
model = tf.lite.Interpreter(model_path="sign_language_model.tflite")
model.allocate_tensors()
input_details = model.get_input_details()
output_details = model.get_output_details()

def preprocess_image(image):
    image = image.resize((96, 96)).convert("RGB")  # Convert to 96x96 RGB
    image = np.array(image, dtype=np.float32) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@prediction_bp.route("/predict", methods=["POST"])
async def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = Image.open(request.files["image"])
    processed_img = preprocess_image(image)

    model.set_tensor(input_details[0]["index"], processed_img)
    model.invoke()
    prediction = model.get_tensor(output_details[0]["index"])

    predicted_sign = chr(np.argmax(prediction) + 65)  # Convert index to A-Z
    confidence = float(np.max(prediction))

    await Prediction.save_prediction(request.json["user_id"], predicted_sign, confidence)
    
    return jsonify({"sign": predicted_sign, "confidence": confidence}), 200
