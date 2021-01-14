import functools
from flask_login import current_user
from flask_socketio import disconnect, emit

from serv.redidb import RediWrap

rw = RediWrap('localhost', 6379)


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            emit('redirect',
                 {'message': 'login'})
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped
