import os
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from config import Config
from routes.users import user_bp
from routes.predictions import prediction_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
JWTManager(app)

# Rate limiting (prevent brute force attacks)
limiter = Limiter(key_func=lambda: request.remote_addr)
limiter.init_app(app)

app.register_blueprint(user_bp, url_prefix="/api/users")
app.register_blueprint(prediction_bp, url_prefix="/api/predict")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Ensure correct port for Render
    app.run(host="0.0.0.0", port=port, debug=True)
