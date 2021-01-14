import redis

from .rmodels import rmodels


class RediWrap():

    def __init__(self, host, port):
        rdb = redis.Redis(host=host,
                          port=port, db=1,
                          decode_responses=True)
        self.totem, self.user, self.totem_skin, self.emote = rmodels(rdb)

    def get_totem(self, totem_id):
        return self.totem.HASH_get(totem_id)

    def get_user(self, user_id):
        return self.user.HASH_get(user_id)

    def get_totem_skin(self, totem_skin_id):
        return self.totem_skin.HASH_get(totem_skin_id)

    def get_emote(self, emote_id):
        return self.emote.HASH_get(emote_id)

    def set_user_totems(self, longitude, latitude, user_id):
        self.user.SET_purge(user_id)
        totems = self.totem.GEO_radius(longitude, latitude, 1)
        for totem in totems:
            self.user.SET_set(user_id, totem)

    def set_totem_location(self, longitude, latitude, totem_id):
        self.totem.GEO_set(totem_id, longitude, latitude)

    def get_totems_in_radius(self, longitude, latitude, radius):
        return self.totem.GEO_radius(longitude, latitude, radius)

    def user_join_totem(self, user_id, totem_id):
        self.totem.SET_set(totem_id, user_id)

    def user_leave_totem(self, user_id, totem_id):
        self.totem.SET_del(totem_id, user_id)

    def check_can_chat(self, user_id, totem_id):
        return self.user.SET_check(user_id, totem_id)
