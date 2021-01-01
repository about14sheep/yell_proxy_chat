from . import db


class Bot(db.Model):
    __tablename__ = 'bots'

    id = db.Column(db.Integer, primary_key=True)
    bot_key = db.Column(db.String(255), unique=True)

    def to_dict(self):
        return {
          'id': self.id,
          'bot_key': self.bot_key
        }
