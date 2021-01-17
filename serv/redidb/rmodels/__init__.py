from serv.models.user import User
from serv.models.emote import Emote

from . import rEmote
from . import rTotem
from . import rTotem_Skin
from . import rUser


def rmodels(redis_db):
    return [rTotem(redis_db),
            rUser(redis_db),
            rTotem_Skin(redis_db),
            rEmote(redis_db)]


def save_user_emote(user_id, emote_id):
    user = User.get_user_by_id(user_id)
    emote = Emote.get_emote_by_id(emote_id)
    return user.collect_emote(emote)
