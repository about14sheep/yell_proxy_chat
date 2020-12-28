from serv.models import Location
from flask import Blueprint, request


location_routes = Blueprint('locations', __name__)


@location_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        locations = Location.locations_in_radius(data['user_geo'], 152)
        if locations:
            return {
                'locations': [location.to_dict() for location in locations]}
        else:
            location = Location.new_location(data)
            return {'new_location': location.to_dict()}
    else:
        locations = Location.query.all()
        return {'locations': [location.to_dict() for location in locations]}


@location_routes.route('/<id>')
def location(id):
    location = Location.query.get(id)
    return {'locations': location.to_dict()}


@location_routes.route('/rad/<rad>/geo/<geo>')
def locations_in_range(rad, geo):
    locations = Location.locations_in_radius(geo, rad)
    return {'locations': [location.to_dict() for location in locations]}
