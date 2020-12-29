from serv.models.location import Location
from flask import Blueprint, request, jsonify


location_routes = Blueprint('locations', __name__)


@location_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        geo = request.json.get('user_geo', None)
        if not geo:
            return jsonify({'error_msg': 'Need location geo'}), 400
        locations = Location.locations_in_radius(geo, 152)
        if locations:
            return {
                'locations': [location.to_dict() for location in locations]}
        else:
            longitude = request.json.get('user_long', None)
            latitude = request.json.get('user_lat', None)
            if not longitude or not latitude:
                return jsonify(
                    {'error_msg': 'Need longitude/latitude for new location'}
                    ), 400
            location = Location.new_location(longitude, latitude)
            return {'new_location': location.to_dict()}
    else:
        locations = Location.query.all()
        return {'locations': [location.to_dict() for location in locations]}


@location_routes.route('/<id>', methods=['GET', 'DELETE'])
def location(id):
    location = Location.get_location(id)
    if request.method == 'DELETE':
        location.delete_location()
        return {'location_deleted': location.to_dict()}
    return {'locations': location.to_dict()}


@location_routes.route('/rad/<rad>/geo/<geo>')
def locations_in_range(rad, geo):
    locations = Location.locations_in_radius(geo, rad)
    return {'locations': [location.to_dict() for location in locations]}


@location_routes.route('/cleanup/all')
def clean_locations():
    Location.delete_expired()
    return jsonify({'msg': 'Cleanup initiated'})
