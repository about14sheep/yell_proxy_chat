from . import Namespace, emit, rw, authenticated_only


class Stream_Socket(Namespace):

    def on_connect(self):
        emit('stream_connect_response',
             {'data': 'Stream Connected'})

    def on_stream_yell(self, data):
        if rw.check_can_chat(data['user_id'], data['totem_id']) == 1:
            rw.user_collect_emote(data['user_id'], data['emote_id'])
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
