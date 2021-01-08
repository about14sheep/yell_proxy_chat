from serv.models.user import User

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from flask_login import login_user, logout_user

session_routes = Blueprint('session', __name__)


@session_routes.route('', methods=['POST', 'PUT', 'DELETE'])
def login():
    if not request.is_json:
        return jsonify({'error_msg': 'Missing JSON in request'})
    if request.method == 'DELETE':
        id = request.json.get('user_id', None)
        user = User.query.get(id)
        user.session_token = None
        user.commit_user()
        logout_user(user)
        return jsonify({'msg': 'Session token removed'})

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({'error_msg': 'Missing email parameter'}), 400
    if not password:
        return jsonify({'error_msg': 'Missing password parameter'}), 400

    if request.method == 'PUT':
        user = User.query.filter(User.email == email).first()
        if not user:
            return jsonify({'error_msg': 'No user with that email'}), 401
        elif not user.check_password(password):
            return jsonify({'error_msg': 'Password is incorrect'}), 401
    if request.method == 'POST':
        username = request.json.get('username', None)
        if not username:
            return jsonify({'error_msg': 'Missing username parameter'}), 400
        user = User(username=username, email=email)
        user.password = password
        user.add_user()

    access_token = create_access_token(identity=email)
    user.session_token = access_token
    login_user(user)
    user.commit_user()
    return {'user': user.to_dict()}
