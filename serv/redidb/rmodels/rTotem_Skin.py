class rTotem_Skin():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, skin):
        for key in skin:
            self.rdb.hset('HTS{}'.format(skin['totem_skin_id']),
                          key, skin[key])

    def HASH_get(self, skin_id):
        return self.rdb.hgetall('HTS{}'.format(totem_skin_id))

    def SET_set(self, skin_id, user_id):
        self.rdb.sadd('STS{}'.format(skin_id), user_id)

    def SET_get(self, skin_id):
        return self.rdb.smembers('STS{}'.format(skin_id))

    def SET_del(self, skin_id, user_id):
        self.rdb.srem('STS{}'.format(skin_id), user_id)

    def SET_check(self, skin_id, user_id):
        return self.rdb.sismember('STS{}'.format(skin_id), user_id)
