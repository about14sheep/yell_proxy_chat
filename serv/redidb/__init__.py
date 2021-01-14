import redis

from .rmodels.rEmote import rEmote
from .rmodels.rTotem import rTotem
from .rmodels.rUser import rUser
from .rmodels.rTotem_Skin import rTotem_Skin


class RediWrap():

    def __init__(self, host, port):
        rdb = redis.Redis(host=host,
                          port=port, db=1,
                          decode_responses=True)
        self.emote = rEmote(rdb)
        self.totem = rTotem(rdb)
        self.user = rUser(rdb)
        self.totem_skin = rTotem_Skin(rdb)

    def set_user_totems(self, longitude, latitude, user_id):
        totems = self.totem.GEO_radius(longitude, latitude, 1)
        for totem in totems:
            self.user.SET_set(user_id, totem)
