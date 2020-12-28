from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    session_token = db.Column(db.String(500))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    geo = db.Column(Geometry(geometry_type="POINT"))

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'user_long': self.longitude,
            'user_lat': self.latitude,
            'username': self.username,
            'session_token': self.session_token,
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

    def add_user(self):
        db.session.add(self)

    def commit_user(self):
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

    def delete_location(self):
        db.session.delete(self)
        db.session.commit()

    def new_location(longitude, latitude):
        location = Location(
            longitude=longitude, latitude=latitude)
        location.update_geo()
        db.session.add(location)
        db.session.commit()
        return location

    def locations_in_radius(geo, rad):
        locations = Location.query.filter(
            func.ST_DistanceSphere(
                Location.geo,
                geo
            ) < rad).all()
        return locations
