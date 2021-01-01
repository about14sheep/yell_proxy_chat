from flask import Blueprint
from serv.models.emote import Emote

emote_routes = Blueprint('emotes', __name__)


@emote_routes.route('')
def index():
    return Emote.get_all_emotes()


@emote_routes.route('/<id>')
def get_emote(id):
    return Emote.get_emote(id)
