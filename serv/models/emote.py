from . import db


class Emote(db.Model):
    __tablename__ = 'emotes'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))

    def to_dict(self):
        return {
          'id': self.id,
          'author_id': self.author_id
        }
