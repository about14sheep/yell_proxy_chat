from flask import Blueprint
from serv.models.totem_skin import Totem_Skin

totem_skin_routes = Blueprint('totem_skins', __name__)


@totem_skin_routes.route('')
def index():
    return Totem_Skin.get_all_skins()


@totem_skin_routes.route('/<id>')
def get_totem_skin(id):
    return Totem_Skin.get_skin(id)
