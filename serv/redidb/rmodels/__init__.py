from . import rEmote
from . import rTotem
from . import rTotem_Skin
from . import rUser


def rmodels(redis_db):
    return [rTotem(redis_db),
            rUser(redis_db),
            rTotem_Skin(redis_db),
            rEmote(redis_db)]
