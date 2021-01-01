from flask import Blueprint
from serv.models.bot import Bot

bot_routes = Blueprint('bots', __name__)


@bot_routes.route('')
def index():
    return Bot.get_all_bots()


@bot_routes.route('/<id>')
def get_bot(id):
    return Bot.get_bot(id)
