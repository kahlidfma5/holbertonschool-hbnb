from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.database import db
from flask_cors import CORS

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config["JWT_SECRET_KEY"] = "your-super-secret-key-here" # Replace with a strong, random key
    
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    
    # Register the users namespace
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
