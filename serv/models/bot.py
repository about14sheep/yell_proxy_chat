from . import db


class Bot(db.Model):
    __tablename__ = 'bots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    bot_key = db.Column(db.String(255), unique=True)

    def to_dict(self):
        return {
          'id': self.id,
          'name': self.name,
          'bot_key': self.bot_key,
          'totems': [totem.to_dict() for totem in self.totems]
        }
