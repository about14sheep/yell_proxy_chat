import redis
from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

from .models import db
from .config import Config
from websocket.login import Login_Socket

from .api.user_routes import user_routes
from .api.session_routes import session_routes
from .api.totem_routes import totem_routes
from .api.totem_skin_routes import totem_skin_routes
from .api.emote_routes import emote_routes
from .api.bot_routes import bot_routes

rdb = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)
login_manager = LoginManager()
socketio = SocketIO(app)
app.config.from_object(Config)

login_manager.init_app(app)
jwt = JWTManager(app)
socketio.on_namespace(Login_Socket('/login'))
db.init_app(app)
CORS(app)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(session_routes, url_prefix='/api/session')
app.register_blueprint(totem_routes, url_prefix='/api/totems')
app.register_blueprint(totem_skin_routes, url_prefix='/api/totem_skins')
app.register_blueprint(emote_routes, url_prefix='/api/emotes')
app.register_blueprint(bot_routes, url_prefix='/api/bots')


if __name__ == '__main__':
    socketio.run(app)
