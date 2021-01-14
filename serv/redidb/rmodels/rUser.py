class rUser():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, user):
        self.rdb.hset(user['user_id'],
                      'username', user['username'])

    def HASH_get(self, user_id):
        return self.rdb.hget(user_id)

    def SET_set(self, user_id, totem_id):
        self.rdb.sadd(user_id, totem_id)

    def SET_get(self, user_id):
        return self.rdb.smembers(user_id)

    def SET_check(self, user_id, totem_id):
        return self.rdb.sismember(user_id, totem_id)
