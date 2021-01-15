from flask_socketio import Namespace, emit

from . import rw, authenticated_only


class Totem_Socket(Namespace):

    def on_connect(self):
        emit('totem_response',
             {'data': 'Totem Socket Connected'})

    def on_totem_save(self, data):
        rw.set_totem({'owner_id': data['owner_id'],
                      'totem_id': data['totem_id'],
                      'totem_skin_id': data['totem_skin_id']})

    def on_totem_get(self, data):
        totem = rw.get_totem(data['totem_id'])
        emit('get_totem_response',
             'data': totem)

    def on_totem_scan(self, data):
        totems = rw.get_totems_in_radius(data['longitude'],
                                         data['latitude'],
                                         data['radius'])
        emit('totems_near', {'totems': totems})

    def on_totem_place(self, data):
        rw.set_totem_location(data['longitude'],
                              data['latitude'],
                              data['totem_id'])

    def on_totem_yell(self, data):
        ismember = rw.check_can_chat(data['user_id'], data['totem_id'])
        if ismember == 1:
            emit('yell_response',
                 {'data': {
                     'username': data['username'],
                     'text': data['text']
                 }}, room=data['totem_id'])
        else:
            emit('yell_response',
                 {'data': {
                     'username': data['username'],
                     'text': 'Get closer to chat!'
                 }})
