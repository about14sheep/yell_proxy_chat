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
