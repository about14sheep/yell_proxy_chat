from serv.models import db, User, Location
from flask import Blueprint, request
from sqlalchemy import func


location_routes = Blueprint('locations', __name__)


@location_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        location = Location(longitude=data['long'], latitude=data['lat'])
        location.update_geo()
        db.session.add(location)
        db.session.commit()
        return {'location added': location.to_dict()}
    else:
        locations = Location.query.all()
        return {'locations': [location.to_dict() for location in locations]}


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
