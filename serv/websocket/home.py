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
        rdb.set('TOTEM_FOR_{}'.format(data['sid']), data['totem_id'])

    def on_yell(self, data):
        ismember = rdb.sismember(data['sid'], data['totem_id'])
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

    def on_channel_details(self, data):
        lname = 'USERS_AT_TOTEM_{}'.format(data['totem_id'])
        users_in_chat = rdb.lrange(lname, 0, 9)
        user_count = rdb.llen(lname)
        emit('join_response',
             {'data': {
                 'users': users_in_chat,
                 'count': user_count
             }})

    def on_join_channel(self, data):
        rdb.lpush(lname, data['username'])
        join_room(data['totem_id'])

    def on_leave_channel(self, data):
        leave_room(data['totem_id'])
        lname = 'USERS_AT_TOTEM_{}'.format(data['totem_id'])
        rdb.lrem(lname, data['username'])
