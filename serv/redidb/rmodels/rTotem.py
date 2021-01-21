class rTotem():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, totem):
        for key in totem:
            self.rdb.hset('HT{}'.format(totem['totem_id']), key, totem[key])

    def HASH_get(self, totem_id):
        totem = self.rdb.hgetall('HT{}'.format(totem_id))
        totem['owner'] = self.rdb.hgetall('HU{}'.format(totem.pop('owner_id')))
        totem['skin'] = self.rdb.hgetall('HTS{}'.format(
                                          totem.pop('totem_skin_id')))
        totem['emote'] = self.rdb.hgetall('HE{}'.format(totem.pop('emote_id')))
        return totem

    def SET_set(self, totem_id, user_id):
        self.rdb.sadd('ST{}'.format(totem_id), user_id)

    def SET_get(self, totem_id):
        return self.rdb.smembers('ST{}'.format(totem_id))

    def SET_check(self, totem_id, user_id):
        return self.rdb.sismember('ST{}'.format(totem_id), user_id)

    def SET_del(self, totem_id, user_id):
        self.rdb.srem('ST{}'.format(totem_id), user_id)

    def SET_count(self, totem_id):
        return self.rdb.scard('ST{}'.format(totem_id))

    def SET_purge(self, totem_id):
        self.rdb.delete('ST{}'.format(totem_id))

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
