from . import db


class Totem_Skin(db.Model):
    __tablename__ = 'totem_skins'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), unique=True, nullable=False)

    totems = db.relationship('Totem', backref='totem_skin')

    @classmethod
    def get_all_skins(cls):
        skins = cls.query.all()
        return {'totem_skins': [skin.to_dict() for skin in skins]}

    @classmethod
    def get_skin(cls, id):
        skin = cls.query.get(id)
        return {'totem_skin': skin.to_dict()}

    def to_dict(self):
        return {
          'id': self.id,
          'image_url': self.image_url
        }
