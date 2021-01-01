from . import db


class Totem_Skin(db.Model):
    __tablename__ = 'totem_skins'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), unique=True, nullable=False)

    totems = db.relationship('Totem', backref='totem_skin')

    def to_dict(self):
        return {
          'id': self.id,
          'image_url': self.image_url
        }
