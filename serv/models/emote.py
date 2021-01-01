from . import db


class Emote(db.Model):
    __tablename__ = 'emotes'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), unique=True, nullable=False)
    author_id = db.Column(
                      db.Integer, db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def get_all_emotes(cls):
        emotes = cls.query.all()
        return {'emotes': [emote.to_dict() for emote in emotes]}

    @classmethod
    def get_emote(cls, id):
        emote = cls.query.get(id)
        return {'emote': emote.to_dict()}

    def to_dict(self):
        return {
          'id': self.id,
          'image_url': self.image_url
        }
