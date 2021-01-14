class rEmote():

    def __init__(self, redis_db):
        self.rdb = redis_db

    def HASH_set(self, emote):
        self.rdb.hset(emote['emote_id'],
                      'image_url', emote['image_url'],
                      'author_id', emote['author_id'])

    def HASH_get(self, emote_id):
        self.rdb.hget(emote_id)

    def SET_set(self, emote_id, user_id):
        self.rdb.sadd(emote_id, user_id)

    def SET_get(self, emote_id):
        return self.smembers(emote_id)

    def SET_check(self, emote_id, user_id):
        return self.sismember(emote_id, user_id)
