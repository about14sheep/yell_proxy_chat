from .models import db, User, Location
from .config import Config

import os
from flask import Flask
from sqlalchemy import func

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


@app.route('/api/locations')
def locations():
    locations = Location.query.all()
    return {'users': [location.to_dict() for location in locations]}


@app.route('/api/locations/<id>')
def location(id):
    location = Location.query.get(id)
    return {'locations': location.to_dict()}


@app.route('/api/locations/rad/<rad>/user/<id>')
def locations_in_range(rad, id):
    usr = User.query.get(id)
    locations = Location.query.filter(func.ST_DistanceSphere(
                                        Location.geo,
                                        usr.geo
                                        ) < rad).all()
    return {'locations': [location.to_dict() for location in locations]}
