from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from config import Config
from routes.users import user_bp
from routes.predictions import prediction_bp
from routes.logs import log_bp

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# JWT Manager
jwt = JWTManager(app)

# Rate limiting to prevent brute-force attacks
limiter = Limiter(app, key_func=lambda: request.remote_addr)

# Register API routes
app.register_blueprint(user_bp, url_prefix="/api/users")
app.register_blueprint(prediction_bp, url_prefix="/api/predict")
app.register_blueprint(log_bp, url_prefix="/api/logs")

if __name__ == "__main__":
    app.run(debug=True)
