from .models import db, User
from .config import Config
import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/api/users')
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@app.route('/api/users/<id>')
def user(id):
    user = User.query.get(id)
    return {'user': user.to_dict()}
