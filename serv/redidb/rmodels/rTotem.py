class rTotem():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, totem):
        for key in totem:
            self.rdb.hset('H{}'.format(totem['totem_id']), key, totem[key])

    def HASH_get(self, totem_id):
        totem = self.rdb.hgetall('H{}'.format(totem_id))
        totem['owner'] = self.rdb.hgetall('H{}'.format(totem.pop('owner_id')))
        totem['skin'] = self.rdb.hgetall('H{}'.format(
                                          totem.pop('totem_skin_id')))
        return totem

    def SET_set(self, totem_id, user_id):
        self.rdb.sadd('S{}'.format(totem_id), user_id)

    def SET_get(self, totem_id):
        return self.rdb.smembers('S{}'.format(totem_id))

    def SET_check(self, totem_id, user_id):
        return self.rdb.sismember('S{}'.format(totem_id), user_id)

    def SET_del(self, totem_id, user_id):
        self.rdb.srem('S{}'.format(totem_id), user_id)

    def SET_count(self, totem_id):
        return self.rdb.scard('S{}'.format(totem_id))

    def SET_purge(self, totem_id):
        self.rdb.delete('S{}'.format(totem_id))

    def GEO_set(self, totem):
        self.rdb.geoadd('totems', totem['longitude'],
                        totem['latitude'], totem['totem_id'])
        self.HASH_set(totem)

    def GEO_radius(self, longitude, latitude, radius):
        tots = self.rdb.georadius('totems', longitude, latitude, radius, 'mi')
        for i, totem_id in enumerate(tots):
            tots[i] = self.HASH_get(totem_id)
        return tots

    def GEO_del(self, totem_id):
        self.rdb.zrem('totems', totem_id)
