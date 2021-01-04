from flask_socketio import Namespace, emit, join_room, leave_room

from . import rdb, authenticated_only


class Home(Namespace):
    # @authenticated_only
    def on_connect(self):
        emit('auth_response',
             {'message': 'user connected'})

    def on_user_location(self, data):
        result_totems = []
        rdb.delete(data['sid'])
        totems = rdb.georadius(data['region'],
                               data['long'],
                               data['lat'],
                               2, 'mi', 'withdist')
        for totem in totems:
            result_totems.append(totem[0])
            if totem[-1] <= 1:
                rdb.sadd(data['sid'], totem[0])
        emit('totems_near', {'totems': result_totems})

    def on_place_totem(self, data):
        rdb.geoadd(data['region'], data['long'], data['lat'],
                   data['totem_id'])

    def on_yell(self, data):
        ismember = rdb.sismember(data['sid'], data['totem_id'])
        if ismember == 1:
            emit('yell_response',
                 {'data': {
                     'username': data['username'],
                     'text': data['text']
                 }}, room=data['totem_id'])

    def on_join_channel(self, data):
        join_room(data['totem_id'])

    def on_leave_channel(self, data):
        leave_room(data['totem_id'])
