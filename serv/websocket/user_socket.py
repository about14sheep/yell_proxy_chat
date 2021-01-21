from . import Namespace, emit, rw, authenticated_only


class User_Socket(Namespace):

    def on_connect(self):
        emit('user_connect',
             {'data': 'User Socket Connected'})

    def on_user_save(self, data):
        rw.set_user({'user_id': data['user_id'],
                     'username': data['username']})
        emit('user_save',
             {'data': 'User {} saved to redis'.format(data['user_id'])})

    def on_user_get(self, data):
        user = rw.get_user(data['user_id'])
        emit('get_user',
             {'data': user})

    def on_user_location(self, data):
        rw.set_user_totems(data['longitude'],
                           data['latitude'],
                           data['user_id'])
        emit('user_location',
             {'data': 'Totems set for User {}'.format(data['user_id'])})

    def on_create_emote(self, data):
        rw.set_emote({'emote_id': data['emote_id'],
                      'image_url': data['image_url'],
                      'author_id': data['user_id']})
