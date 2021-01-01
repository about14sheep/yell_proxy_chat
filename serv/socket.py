from flask_socketio import Namespace, emit, join_room, leave_room

from .models.user import User


class WebSocket(Namespace):
    def on_join(self, message):
        join_room(message['location_id'])
        emit('join_response',
             {'data': [user.to_dict() for user in active_users]},
             room=message['location_id'])

    def on_leave(self, message):
        leave_room(message['location_id'])
        emit('leave_response',
             {'data': message['user_id']}, room=message['location_id'])

    def on_yell(self, message):
        emit('yell_response',
             {'data': message}, room=message['location_id'])

    def on_whisper(self, message):
        emit('whisper_response',
             {'data': message}, room=message['location_id'])
