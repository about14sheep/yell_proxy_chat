from flask_socketio import leave_room, join_room

from . import Namespace, emit, rw, authenticated_only


class Totem_Socket(Namespace):

    def on_connect(self):
        emit('totem_connect',
             {'data': 'Totem Socket Connected'})

    def on_totem_save(self, data):
        rw.set_totem({'owner_id': data['owner_id'],
                      'totem_id': data['totem_id'],
                      'totem_skin_id': data['totem_skin_id']})
        emit('totem_save',
             {'data': 'Totem {} saved to redis'.format(data['totem_id'])})

    def on_totem_get(self, data):
        totem = rw.get_totem(data['totem_id'])
        emit('get_totem', {'data': totem})

    def on_totem_scan(self, data):
        totems = rw.get_totems_in_radius(data['longitude'],
                                         data['latitude'],
                                         data['radius'])
        emit('totems_near', {'data': totems})

    def on_totem_place(self, data):
        rw.set_totem_location(data['longitude'],
                              data['latitude'],
                              data['totem_id'])
        emit('totem_place', data, broadcast=True)

    def on_totem_join(self, data):
        rw.user_join_totem(data['user_id'], data['totem_id'])
        join_room(data['totem_id'])
        emit('totem_join',
             {'data': 'Connected to totem {}'.format(data['totem_id'])})

    def on_totem_leave(self, data):
        rw.user_leave_totem(data['user_id'], data['totem_id'])
        leave_room(data['totem_id'])
        emit('totem_leave',
             {'data': 'Disconnected from totem {}'.format(data['totem_id'])})

    def on_totem_skin_save(self, data):
        rw.set_totem_skin(data)
        emit('totem_skin_save', {'data': data})
