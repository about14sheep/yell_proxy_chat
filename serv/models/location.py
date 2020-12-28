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

    @classmethod
    def delete_expired(cls):
        limit = datetime.now() - timedelta(minutes=5)
        print(limit)
        cls.query.filter(cls.timestamp >= limit).delete()
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'timestamp': self.timestamp
        }

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)

    def delete_location(self):
        db.session.delete(self)
        db.session.commit()

    def update_timestamp(self):
        self.timestamp = datetime.utcnow()
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
