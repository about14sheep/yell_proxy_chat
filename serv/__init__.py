# import eventlet
# eventlet.monkey_patch()  # noqa

from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

from .models import db
from .models.user import User
from .config import Config

from .websocket.totem_socket import Totem_Socket
from .websocket.user_socket import User_Socket
from .websocket.stream_socket import Stream_Socket

from .api.user_routes import user_routes
from .api.session_routes import session_routes
from .api.totem_routes import totem_routes
from .api.totem_skin_routes import totem_skin_routes
from .api.emote_routes import emote_routes
from .api.bot_routes import bot_routes


app = Flask(__name__)
login_manager = LoginManager()
socketio = SocketIO(app)
app.config.from_object(Config)
login_manager.init_app(app)
db.init_app(app)

socketio.on_namespace(Totem_Socket('/totem'))
socketio.on_namespace(User_Socket('/user'))
socketio.on_namespace(Stream_Socket('/stream'))

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(session_routes, url_prefix='/api/session')
app.register_blueprint(totem_routes, url_prefix='/api/totems')
app.register_blueprint(totem_skin_routes, url_prefix='/api/totem_skins')
app.register_blueprint(emote_routes, url_prefix='/api/emotes')
app.register_blueprint(bot_routes, url_prefix='/api/bots')

jwt = JWTManager(app)
CORS(app)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.get_user_by_id(int(user_id))
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return {'message': 'youre trash kid'}


if __name__ == '__main__':
    socketio.run(app, message_queue='redis://')
