from . import db, Geometry
from datetime import datetime, timedelta
from sqlalchemy import func


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    geo = db.Column(Geometry(geometry_type="POINT"))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    users = db.relationship('User')

    @classmethod
    def delete_expired(cls):
        limit = datetime.now() - timedelta(minutes=5)
        cls.query.filter(cls.timestamp >= limit).delete()
        db.session.commit()

    @classmethod
    def new_location(cls, longitude, latitude):
        location = cls(
            longitude=longitude, latitude=latitude)
        location.update_geo()
        db.session.add(location)
        db.session.commit()
        return location

    @classmethod
    def get_location(cls, id):
        return cls.query.get(id)

    @classmethod
    def join_user_to_location(cls, id, user):
        location = cls.get_location(id)
        location.users.append(user)
        db.session.commit()

    @classmethod
    def remove_user_from_location(cls, id, user):
        location = cls.get_location(id)
        location.users.remove(user)
        db.session.commit()

    @classmethod
    def update_timestamp_for_location(cls, id):
        location = cls.get_location(id)
        location.timestamp = datetime.utcnow()
        db.session.commit()

    def delete_location(self):
        db.session.delete(self)
        db.session.commit()

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)

    def commit_location(self):
        db.session.commit()

    def locations_in_radius(geo, rad):
        locations = Location.query.filter(
            func.ST_DistanceSphere(
                Location.geo,
                geo
            ) < rad).all()
        return locations

    def to_dict(self):
        return {
            'id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'timestamp': self.timestamp,
            'users': [user.to_dict() for user in self.users]
        }
