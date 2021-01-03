import redis
import functools
from flask_login import current_user
from flask_socketio import disconnect, emit


rdb = redis.Redis(host='localhost', port=6379, db=0)
rdb.geoadd('tokyo', 139.839478, 35.652832, 'your mom',
           139.844444, 35.678987, 'his mom',
           139.896595, 35.688955, 'their mom')


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
