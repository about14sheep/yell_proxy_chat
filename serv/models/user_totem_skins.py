from . import db

user_totem_skins = db.Table('user_totem_skins',
                            db.Column('user_id', db.Integer,
                                      db.ForeignKey('users.id',
                                                    primary_key=True)),
                            db.Column('totem_skin_id', db.Integer,
                                      db.ForeignKey('totem_skins.id',
                                                    primary_key=True)))


class User_Totem_Skin(db.Model):
    __tablename__ = 'user_totem_skins'

    id = db.Column(db.Integer, primary_key=True)
