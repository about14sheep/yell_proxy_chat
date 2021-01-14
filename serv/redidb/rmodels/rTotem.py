class rTotem():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, totem):
        self.rdb.hset(totem['totem_id'],
                      'owner_id', totem['owner_id'],
                      'totem_skin_id', totem['totem_skin_id'])

    def HASH_get(self, totem_id):
        return self.rdb.hget(totem_id)

    def SET_set(self, totem_id, user_id):
        self.rdb.sadd(totem_id, user_id)

    def SET_check(self, totem_id, user_id):
        return self.rdb.sismember(totem_id, user_id)

    def SET_get(self, totem_id):
        return self.rdb.smembers(totem_id)

    def SET_count(self, totem_id):
        return self.rdb.scard(totem_id)

    def GEO_set(self, totem_id, longitude, latitude):
        self.rdb.geoadd('totems', longitude, latitude, totem_id)

    def GEO_radius(self, longitude, latitude, radius):
        return self.rdb.georadius('totems', longitude, latitude, radius, 'mi')
