from .models import db
from .config import Config

from .api.user_routes import user_routes
from .api.location_routes import location_routes
from .api.session_routes import session_routes

from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
login_manager = LoginManager()
app.config.from_object(Config)

login_manager.init_app(app)
jwt = JWTManager(app)
db.init_app(app)
CORS(app)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(location_routes, url_prefix='/api/locations')
app.register_blueprint(session_routes, url_prefix='/api/session')
