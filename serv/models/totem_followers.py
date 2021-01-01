from . import db

follows = db.Table('follows',
                   db.Column('user_id', db.Integer,
                             db.ForeignKey('users.id'), primary_key=True),
                   db.Column('totem_id', db.Integer,
                             bd.ForeignKey('totems.id', primary_key=True)))


class Totem_Follower(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
