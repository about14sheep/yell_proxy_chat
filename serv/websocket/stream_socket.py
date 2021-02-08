from flask_socketio import leave_room, join_room, close_room

from . import Namespace, emit, rw, authenticated_only


class Stream_Socket(Namespace):

    def on_connect(self):
        emit('stream_connect', {'data': 'Stream Socket Connected'})

    def on_stream_yell(self, data):
        msg = {'username': data['username'], 'text': data['text']}
        if rw.check_can_chat(data['user_id'], data['totem_id']) == 1:
            emote = rw.user_collect_emote(data['user_id'], data['emote_id'])
            if emote:
                emit('new_emote', {'data': emote})
            emit('stream_yell', {'data': msg}, room=data['totem_id'])
        else:
            msg['text'] = 'Get closer to chat!'
            emit('stream_yell', {'data': msg})

    def on_totem_join(self, data):
        rw.user_join_totem(data['user_id'], data['totem_id'])
        totem = rw.get_totem(data['totem_id'])
        join_room(data['totem_id'])
        emit('totem_join',
             {'data': totem})

    def on_totem_leave(self, data):
        rw.user_leave_totem(data['user_id'], data['totem_id'])
        leave_room(data['totem_id'])
        emit('totem_leave',
             {'data': 'Disconnected from totem {}'.format(data['totem_id'])})

    def on_close_room(self, data):
        emit('room_closing', {'data': data['totem_id']}, room=data['totem_id'])
        close_room(data['totem_id'])
