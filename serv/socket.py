from flask_socketio import Namespace, emit, join_room, leave_room

from .models.location import Location
from .models.user import User


class WebSocket(Namespace):
    def on_join(self, message):
        join_room(message['location_id'])
        Location.join_user_to_location(
                  message['location_id'], User.get_user(message['user_id']))

    def on_leave(self, message):
        leave_room(message['location_id'])
        Location.remove_user_from_location(
                  message['location_id'], User.get_user(message['user_id']))

    def on_message(self, message):
        Location.update_timestamp_for_location(message['location_id'])
        emit('message_response',
             {'data': message}, room=message['location_id'])
