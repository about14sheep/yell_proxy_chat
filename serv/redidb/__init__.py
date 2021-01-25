import redis

from .rmodels import rmodels_factory, SQL_Interface


class RediWrap():

    def __init__(self, host, port):
        rdb = redis.Redis(host=host,
                          port=port, db=1,
                          decode_responses=True)
        (self.totem,
         self.user,
         self.totem_skin,
         self.emote) = rmodels_factory(rdb)

    def set_totem(self, totem):
        self.totem.HASH_set(totem)

    def set_user(self, user):
        self.user.HASH_set(user)

    def set_totem_skin(self, totem_skin):
        self.totem_skin.HASH_set(totem_skin)

    def set_emote(self, emote):
        self.emote.HASH_set(emote)

    def get_totem(self, totem_id):
        totem = self.totem.HASH_get(totem_id)
        totem['emote'] = self.get_emote(totem.pop('emote_id'))
        totem['owner'] = self.get_user(totem.pop('owner_id'))
        totem['skin'] = self.get_totem_skin(totem.pop('totem_skin_id'))
        return totem

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
        self.totem.GEO_set({'totem_id': totem_id,
                            'longitude': longitude,
                            'latitude': latitude})

    def delete_totem_location(self, totem_id):
        self.totem.SET_purge(totem_id)
        self.totem.GEO_del(totem_id)

    def get_totems_in_radius(self, longitude, latitude, radius):
        tots = self.totem.GEO_radius(longitude, latitude, radius)
        for i, totem_id in enumerate(tots):
            tots[i] = self.get_totem(totem_id)
        return tots

    def user_join_totem(self, user_id, totem_id):
        self.totem.SET_set(totem_id, user_id)

    def user_leave_totem(self, user_id, totem_id):
        self.totem.SET_del(totem_id, user_id)

    def check_can_chat(self, user_id, totem_id):
        return self.user.SET_check(user_id, totem_id)

    def user_collect_emote(self, user_id, emote_id):
        if self.emote.SET_check(emote_id, user_id) != 1:
            self.emote.SET_set(emote_id, user_id)
            return SQL_Interface.save_user_emote(user_id, emote_id)
