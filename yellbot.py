import socketio

sio = socketio.Client()


sio.connect('http://127.0.0.1:5000', namespaces=['/totem', '/stream', '/user'])


@sio.on('connect', namespace='/totem')
def on_connect():
    sio.emit('totem_place',
             {
                 'latitude': 36.174465,
                 'longitude': -86.767960,
                 'totem_id': 1,
             }, namespace='/totem')
    # sio.emit('user_location',
    #          {
    #              'sid': sio.sid,
    #              'lat': 35.652832,
    #              'long': 139.839478,
    #              'region': 'tokyo'
    #          }, namespace='/home')


@sio.on('totem_place_response', namespace='/totem')
def on_auth(data):
    print(data)


@sio.on('redirect', namespace='/totem')
def on_signoff(data):
    print(data)
