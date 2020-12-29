from . import db, Geometry
from werkzeug.security import generate_password_hash, check_password_hash


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

    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    @classmethod
    def get_user(cls, id):
        return cls.query.get(id)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_position(self):
        self.update_geo()
        self.commit_user()

    def delete_user(self):
        db.session.delete(self)
        self.commit_user()

    def add_user(self):
        db.session.add(self)

    def commit_user(self):
        db.session.commit()

    def update_geo(self):
        self.geo = 'POINT({} {})'.format(self.longitude, self.latitude)

    def to_dict(self):
        return {
            'id': self.id,
            'user_long': self.longitude,
            'user_lat': self.latitude,
            'username': self.username,
            'session_token': self.session_token,
            'user_geo': '{}'.format(self.geo)
        }
