from flask_socketio import Namespace, emit, join_room, leave_room

from .models.location import Location
from .models.user import User


class WebSocket(Namespace):
    def on_join(self, message):
        join_room(message['location_id'])
        active_users = Location.join_user_to_location(
                  message['location_id'], User.get_user(message['user_id']))
        emit('join_response',
             {'data': [user.to_dict() for user in active_users]},
             room=message['location_id'])

    def on_leave(self, message):
        leave_room(message['location_id'])
        Location.remove_user_from_location(
                  message['location_id'], User.get_user(message['user_id']))
        emit('leave_response',
             {'data': message['user_id'], room=message['location_id']})

    def on_yell(self, message):
        Location.update_timestamp_for_location(message['location_id'])
        emit('yell_response',
             {'data': message}, room=message['location_id'])

    def on_whisper(self, message):
        Location.update_timestamp_for_location(message['location_id'])
        emit('whisper_response',
             {'data': message}, room=message['location_id'])
