from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from sqlalchemy import func

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    geo = db.Column(Geometry(geometry_type="POINT"))

    def to_dict(self):
        return {
          'id': self.id,
          'user_long': self.longitude,
          'user_lat': self.latitude,
          'username': self.username,
          'user_geo': '{}'.format(self.geo)
        }

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)

    def update_position(self):
        self.update_geo()
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    geo = db.Column(Geometry(geometry_type="POINT"))

    def to_dict(self):
        return {
          'id': self.id,
          'longitude': self.longitude,
          'latitude': self.latitude
        }

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)

    def new_location(data):
        location = Location(
            longitude=data['user_long'], latitude=data['user_lat'])
        location.update_geo()
        db.session.add(location)
        db.session.commit()
        return location

    def delete_location(self):
        db.session.delete(self)
        db.session.commit()

    def locations_in_radius(geo, rad):
        locations = Location.query.filter(
                                      func.ST_DistanceSphere(
                                        Location.geo,
                                        geo
                                      ) < rad).all()
        return locations
