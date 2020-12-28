from serv.models.user import User
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
        longitude = request.json.get('user_long', None)
        latitude = request.json.get('user_lat', None)
        if not longitude or not latitude:
            return jsonify(
                    {'error_msg': 'Need longitude/latitude for user position'}
                    ), 400
        user.longitude = longitude
        user.latitude = latitude
        user.update_position()
    if request.method == 'DELETE':
        user.delete_user()
        return {'user_deleted': user.to_dict()}
    return {'user': user.to_dict()}
