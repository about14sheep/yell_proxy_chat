from . import db

bots = db.Table('totem_bots',
                db.Column('bot_id', db.Integer,
                          db.ForeignKey('bots.id'), primary_key=True),
                db.Column('totem_id', db.Integer,
                          db.ForeignKey('totems.id', primary_key=True)))


class Totem_Bot(db.Model):
    __tablename__ = 'totem_bots'

    id = db.Column(db.Integer, primary_key=True)
