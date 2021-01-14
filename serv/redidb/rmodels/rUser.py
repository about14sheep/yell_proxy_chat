class rUser():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, user):
        self.rdb.hset('H{}'.format(user['user_id']),
                      'username', user['username'],
                      'user_id', user['user_id'])

    def HASH_get(self, user_id):
        return self.rdb.hget('H{}'.format(user_id))

    def SET_set(self, user_id, totem_id):
        self.rdb.sadd('S{}'.format(user_id), totem_id)

    def SET_get(self, user_id):
        return self.rdb.smembers('S{}'.format(user_id))

    def SET_del(self, user_id, totem_id):
        self.rdb.srem('S{}'.format(user_id), totem_id)

    def SET_purge(self, user_id):
        self.rdb.delete('S{}'.format(user_id))

    def SET_check(self, user_id, totem_id):
        return self.rdb.sismember('S{}'.format(user_id), totem_id)
