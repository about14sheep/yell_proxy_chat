from flask_socketio import Namespace, emit, join_room, leave_room

from . import rw, authenticated_only


class Home(Namespace):
    # @authenticated_only
    def on_connect(self):
        emit('auth_response',
             {'message': 'user connected'})

    def on_user_location(self, data):
        rw.set_user_totems(data['region'],
                           data['long'],
                           data['lat'],
                           data['user_id'])

    def on_totem_scan(self, data):
        totems = rw.get_totems_in_radius(data['region'],
                                         data['long'],
                                         data['lat'],
                                         2)
        emit('totems_near', {'totems': totems})

    def on_place_totem(self, data):
        rw.set_totem_location(data['region'], data['long'], data['lat'],
                              data['totem_id'])
        rw.set_user_totem_id(data['user_id'], data['totem_id'])

    def on_yell(self, data):
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

    def on_totem_details(self, data):
        data = rw.get_totem_details(data['totem_id'])
        emit('totem_details_response', {'data': data})

    def on_join_channel(self, data):
        rw.user_join_totem(data['user_id'], data['totem_id'])
        join_room(data['totem_id'])

    def on_leave_channel(self, data):
        rw.user_join_totem(data['user_id'], data['totem_id'])
        leave_room(data['totem_id'])
