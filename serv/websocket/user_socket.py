from flask_socketio import Namespace, emit

from . import rw, authenticated_only


class User_Socket(Namespace):

    def on_connect(self):
        emit('user_response',
             {'data': 'User Socket Connected'})

    def on_user_save(self, data):
        rw.set_user({'user_id': data['user_id'],
                     'username': data['username']})

    def on_user_get(self, data):
        user = rw.get_user(data['user_id'])
        emit('get_user_response',
             'data': user)

    def on_user_location(self, data):
        rw.set_user_totems(data['longitude'],
                           data['latitude'],
                           data['user_id'])
