from serv.models import User
from flask import Blueprint, request

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def index():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def user(id):
    user = User.query.get(id)
    if request.method == 'PUT':
        data = request.json
        user.longitude = data['long']
        user.latitude = data['lat']
        user.update_position()
    if request.method == 'DELETE':
        user.delete_user()
        return {'user_deleted': user.to_dict()}
    return {'user': user.to_dict()}
