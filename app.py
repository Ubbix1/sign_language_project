from flask import Flask
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
limiter = Limiter(app, key_func=lambda: request.remote_addr)

app.register_blueprint(user_bp, url_prefix="/api/users")
app.register_blueprint(prediction_bp, url_prefix="/api/predict")

if __name__ == "__main__":
    app.run(debug=True)
