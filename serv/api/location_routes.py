from serv.models import Location
from flask import Blueprint, request


location_routes = Blueprint('locations', __name__)


@location_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        locations = Location.locations_in_radius(data['user_id'], 152)
        if locations:
            return {
                'locations': [location.to_dict() for location in locations]}
        else:
            location = Location.new_location(data['user_id'])
            return {'new_location': location.to_dict()}
    else:
        locations = Location.query.all()
        return {'locations': [location.to_dict() for location in locations]}


@location_routes.route('/<id>')
def location(id):
    location = Location.query.get(id)
    return {'locations': location.to_dict()}


@location_routes.route('/rad/<rad>')
def locations_in_range(rad):
    data = request.json
    locations = Location.locations_in_radius(data['user_id'], rad)
    return {'locations': [location.to_dict() for location in locations]}
