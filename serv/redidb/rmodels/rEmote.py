class rEmote():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, emote):
        self.rdb.hset('H{}'.format(emote['emote_id']),
                      'emote_id', emote['emote_id'],
                      'image_url', emote['image_url'],
                      'author_id', emote['author_id'])

    def HASH_get(self, emote_id):
        self.rdb.hget('H{}'.format(emote_id))

    def SET_set(self, emote_id, user_id):
        self.rdb.sadd('S{}'.format(emote_id), user_id)

    def SET_get(self, emote_id):
        return self.rdb.smembers('S{}'.format(emote_id))

    def SET_del(self, emote_id, user_id):
        return self.rdb.srem('S{}'.format(emote_id), user_id)

    def SET_check(self, emote_id, user_id):
        return self.sismember('S{}'.format(emote_id), user_id)
