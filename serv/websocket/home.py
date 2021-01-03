from flask_socketio import Namespace, emit

from . import authenticated_only


class Home(Namespace):
    @authenticated_only
    def on_connect(self, message):
        emit('auth_response',
             {'message': '{} has joined'.format(current_user.username)},
             broadcast=True)
