from serv.models import User, Location
from flask import Blueprint
from sqlalchemy import func


location_routes = Blueprint('locations', __name__)


@location_routes.route('/')
def index():
    locations = Location.query.all()
    return {'users': [location.to_dict() for location in locations]}


@location_routes.route('/<id>')
def location(id):
    location = Location.query.get(id)
    return {'locations': location.to_dict()}


@location_routes.route('/rad/<rad>/user/<id>')
def locations_in_range(rad, id):
    usr = User.query.get(id)
    locations = Location.query.filter(
                                      func.ST_DistanceSphere(
                                        Location.geo,
                                        usr.geo
                                      ) < rad).all()
    return {'locations': [location.to_dict() for location in locations]}
