class rEmote():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, emote):
        for key in emote:
            self.rdb.hset('HE{}'.format(emote['emote_id']), key, emote[key])

    def HASH_get(self, emote_id):
        return self.rdb.hgetall('HE{}'.format(emote_id))

    def SET_set(self, emote_id, user_id):
        self.rdb.sadd('SE{}'.format(emote_id), user_id)

    def SET_get(self, emote_id):
        return self.rdb.smembers('SE{}'.format(emote_id))

    def SET_del(self, emote_id, user_id):
        return self.rdb.srem('SE{}'.format(emote_id), user_id)

    def SET_check(self, emote_id, user_id):
        return self.rdb.sismember('SE{}'.format(emote_id), user_id)
