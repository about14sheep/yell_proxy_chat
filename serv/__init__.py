from .models import db
from .config import Config
from .socket import WebSocket

from .api.user_routes import user_routes
from .api.session_routes import session_routes

from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

app = Flask(__name__)
login_manager = LoginManager()
socketio = SocketIO(app)
app.config.from_object(Config)

login_manager.init_app(app)
jwt = JWTManager(app)
socketio.on_namespace(WebSocket('/chat'))
db.init_app(app)
CORS(app)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(session_routes, url_prefix='/api/session')

if __name__ == '__main__':
    socketio.run(app)
