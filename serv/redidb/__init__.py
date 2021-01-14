import redis

from .rmodels import rmodels


class RediWrap():

    def __init__(self, host, port):
        rdb = redis.Redis(host=host,
                          port=port, db=1,
                          decode_responses=True)
        self.totem,
        self.user,
        self.totem_skin,
        self.emote = rmodels(rdb)

    def set_user_totems(self, longitude, latitude, user_id):
        totems = self.totem.GEO_radius(longitude, latitude, 1)
        for totem in totems:
            self.user.SET_set(user_id, totem)
