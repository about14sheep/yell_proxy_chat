from . import db


class Bot(db.Model):
    __tablename__ = 'bots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    bot_key = db.Column(db.String(255), unique=True)

    @classmethod
    def get_all_bots(cls):
        bots = cls.query.all()
        return {'bots': [bot.to_dict() for bot in bots]}

    @classmethod
    def get_bot_by_id(cls, id):
        bot = cls.query.get(id)
        return {'bot': bot.to_dict()}

    def to_dict(self):
        return {
          'id': self.id,
          'name': self.name,
          'bot_key': self.bot_key,
          'totems': [{
                      'id': totem.id,
                      'totem_skin_id': totem.totem_skin_id
                      } for totem in self.totems]
        }
