from flask import Blueprint
from serv.models.user import User

user_routes = Blueprint('users', __name__)


@user_routes.route('')
def index():
    return User.get_all_users()


@user_routes.route('/<id>')
def user(id):
    return User.get_user_by_id(id)
