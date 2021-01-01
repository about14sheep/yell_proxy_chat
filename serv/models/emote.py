from . import db


class Emote(db.Model):
    __tablename__ = 'emotes'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), unique=True, nullable=False)
    author_id = db.Column(
                      db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
          'id': self.id,
          'image_url': self.image_url,
          'author_id': self.author_id
        }
