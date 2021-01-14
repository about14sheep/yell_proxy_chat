class rTotem_Skin():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, skin):
        self.rdb.hset('H{}'.format(skin['totem_skin_id']),
                      'image_url', skin['image_url'],
                      'totem_skin_id', skin['totem_skin_id'])

    def HASH_get(self, skin_id):
        return self.rdb.hget('H{}'.format(totem_skin_id))

    def SET_set(self, skin_id, user_id):
        self.rdb.sadd('S{}'.format(totem_skin_id), user_id)

    def SET_get(self, skin_id):
        return self.rdb.smembers('S{}'.format(totem_skin_id))

    def SET_check(self, skin_id, user_id):
        return self.rdb.sismember('S{}'.format(totem_skin_id), user_id)
