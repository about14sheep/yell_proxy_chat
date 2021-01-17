from . import Namespace, emit, rw, authenticated_only


class Stream_Socket(Namespace):

    def on_connect(self):
        emit('stream_connect_response',
             {'data': 'Stream Connected'})

    def on_stream_yell(self, data):
        data = {
            'username': data['username'],
            'text': data['text']
        }
        if rw.check_can_chat(data['user_id'], data['totem_id']) == 1:
            emote = rw.user_collect_emote(data['user_id'], data['emote_id'])
            if emote:
                data['emote'] = emote
            emit('yell_response', {'data': data}, room=data['totem_id'])
        else:
            data['text'] = 'Get closer to chat!'
            emit('yell_response', {'data': data})
