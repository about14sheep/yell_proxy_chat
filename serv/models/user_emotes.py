from . import db


emotes = db.Table('user_emotes',
                  db.Column('user_id', db.Integer,
                            db.ForeignKey('users.id', primary_key=True)),
                  db.Column('emote_id', db.Integer,
                            db.ForeignKey('emotes.id', primary_key=True)))


class User_Emote(db.Model):
    __tablename__ = 'user_emotes'

    id = db.Column(db.Integer, primary_key=True)
