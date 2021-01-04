from flask_socketio import Namespace, emit, join_room, leave_room

from . import rdb, authenticated_only


class Home(Namespace):
    # @authenticated_only
    def on_connect(self):
        emit('auth_response',
             {'message': 'user connected'})

    def on_user_location(self, data):
        rdb.geoadd(data['region'], data['long'], data['lat'], data['sid'])
        totems = rdb.georadius(data['region'],
                               data['long'],
                               data['lat'],
                               2, 'mi')
        emit('totems_near', {'totems': totems})

    def on_place_totem(self, data):
        rdb.geoadd(data['region'], data['long'], data['lat'],
                   '{}'.format(data['totem']))

    def on_yell(self, data):
        dist = rdb.geodist(data['region'], data['sid'], data['totem_id'], 'mi')
        if dist <= 1:
            emit('yell_response',
                 {'data': {
                     'username': data['username'],
                     'text': data['text']
                 }}, room=data['totem_id'])

    def on_join_channel(self, data):
        join_room(data['totem_id'])

    def on_leave_channel(self, data):
        leave_room(data['totem_id'])
