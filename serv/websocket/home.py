from flask_socketio import Namespace, emit

from . import rdb, authenticated_only


class Home(Namespace):
    # @authenticated_only
    def on_connect(self):
        emit('auth_response',
             {'message': 'user connected'})

    def on_user_location(self, data):
        places = rdb.georadius(data['region'],
                               data['long'],
                               data['lat'],
                               200, 'km')
        print(places)

    def on_success(self, data):
        print(data)
