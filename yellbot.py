import socketio

sio = socketio.Client()


sio.connect('http://127.0.0.1:5000', namespaces=['/chat'])


@sio.on('connect', namespace='/chat')
def on_connect():
    print('yellbot has entered the chat')
    sio.emit('join', {'user_id': 1, 'location_id': 1}, namespace='/chat')


@sio.on('join_response', namespace='/chat')
def on_join_response(data):
    print('Room joined, server returned: ', data)
