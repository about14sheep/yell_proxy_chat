from . import db

follows = db.Table('follows',
                   db.Column('user_id', db.Integer,
                             db.ForeignKey('users.id'), primary_key=True),
                   db.Column('totem_id', db.Integer,
                             db.ForeignKey('totems.id'), primary_key=True))

bots = db.Table('totem_bots',
                db.Column('bot_id', db.Integer,
                          db.ForeignKey('bots.id'), primary_key=True),
                db.Column('totem_id', db.Integer,
                          db.ForeignKey('totems.id'), primary_key=True))


class Totem(db.Model):
    __tablename__ = 'totems'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    totem_skin_id = db.Column(
        db.Integer, db.ForeignKey('totem_skins.id'), nullable=False)

    bots = db.relationship('Bot', secondary=bots, lazy='subquery',
                           backref=db.backref('totems', lazy=True))

    followers = db.relationship('User', secondary=follows, lazy='subquery',
                                backref=db.backref('followed_totems'))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'totem_skin_id': self.totem_skin_id,
            'bots': [bot.to_dict() for bot in self.bots],
            'followers': [user.to_dict() for user in self.followers]
        }
