from flask import Blueprint
from serv.models.totem import Totem

totem_routes = Blueprint('totems', __name__)


@totem_routes.route('')
def index():
    return Totem.get_all_totems()


@totem_routes.route('/<id>')
def get_totem(id):
    return Totem.get_totem(id)
