import socketio

sio = socketio.Client()


sio.connect('http://127.0.0.1:5000', namespaces=['/home'])


@sio.on('connect', namespace='/home')
def on_connect():
    sio.emit('auth',
             {'message': {'user_id': 1}}, namespace='/home')


@sio.on('auth_response', namespace='/home')
def on_auth(data):
    print(data)


@sio.on('redirect', namespace='/home')
def on_signoff(data):
    print(data)
