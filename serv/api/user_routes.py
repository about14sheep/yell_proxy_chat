from serv.models import User
from flask import Blueprint

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def index():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<id>')
def user(id):
    user = User.query.get(id)
    return {'user': user.to_dict()}
