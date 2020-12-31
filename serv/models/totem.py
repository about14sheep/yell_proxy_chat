from . import db


class Totem(db.Model):
    __tablename__ = 'totems'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))
    totem_skin_id = db.Column(
        db.Integer, db.ForeignKey('totemskin.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'totem_skin_id': self.totem_skin_id
        }
