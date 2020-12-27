from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

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
          'longitude': self.longitude,
          'latitude': self.latitude,
          'username': self.username,
          'geo': '{}'.format(self.geo),
        }

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)


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
          'latitude': self.latitude,
          'geo': '{}'.format(self.geo),
        }

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)
