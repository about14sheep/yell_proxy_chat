import socketio

sio = socketio.Client()


sio.connect('http://127.0.0.1:5000', namespaces=['/home'])


@sio.on('connect', namespace='/home')
def on_connect():
    # sio.emit('place_totem',
    #          {
    #              'lat': 35.652832,
    #              'long': 139.839478,
    #              'region': 'tokyo',
    #              'totem': {
    #                  'id': 1,
    #                  'image_url': 'yourmom.png',
    #              }
    #          }, namespace='/home')
    sio.emit('user_location',
             {
                 'sid': sio.sid,
                 'lat': 35.652832,
                 'long': 139.839478,
                 'region': 'tokyo'
             }, namespace='/home')


@sio.on('totems_near', namespace='/home')
def on_auth(data):
    print(data)


@sio.on('redirect', namespace='/home')
def on_signoff(data):
    print(data)
