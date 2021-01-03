from flask_login import current_user
from flask_socketio import Namespace

from serv.models.user import User


class Login_Socket(Namespace):
    def on_connect(self, message):
        if current_user.is_authenticated:
            emit('auth_response',
                 {'message': '{} has joined'.format(current_user.username)},
                 broadcast=True)
        else:
            return False
