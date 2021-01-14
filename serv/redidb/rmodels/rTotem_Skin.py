class rTotem_Skin():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, skin):
        self.rdb.hset(skin['totem_skin_id'],
                      'image_url', skin['image_url'])

    def HASH_get(self, skin_id):
        return self.rdb.hget(skin_id)

    def SET_set(self, skin_id, user_id):
        self.rdb.sadd(skin_id, user_id)

    def SET_get(self, skin_id):
        return self.rdb.smembers(skin_id)

    def SET_check(self, skin_id, user_id):
        return self.rdb.sismember(skin_id, user_id)
