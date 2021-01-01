from . import db
from werkzeug.security import generate_password_hash, check_password_hash

emotes = db.Table('user_emotes',
                  db.Column('user_id', db.Integer,
                            db.ForeignKey('users.id'), primary_key=True),
                  db.Column('emote_id', db.Integer,
                            db.ForeignKey('emotes.id'), primary_key=True))

user_totem_skins = db.Table('user_totem_skins',
                            db.Column('user_id', db.Integer,
                                      db.ForeignKey('users.id'),
                                      primary_key=True),
                            db.Column('totem_skin_id', db.Integer,
                                      db.ForeignKey('totem_skins.id'),
                                      primary_key=True))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    session_token = db.Column(db.String(500))

    user_totem = db.relationship('Totem', backref='user')

    authored_emotes = db.relationship('Emote', backref='author')

    emotes = db.relationship('Emote',
                             secondary=emotes, lazy='subquery',
                             backref=db.backref('users', lazy=True))

    totem_skins = db.relationship('Totem_Skin',
                                  secondary=user_totem_skins, lazy='subquery',
                                  backref=db.backref('users', lazy=True))

    @classmethod
    def get_user(cls, id):
        return cls.query.get(id)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def delete_user(self):
        db.session.delete(self)
        self.commit_user()

    def add_user(self):
        db.session.add(self)

    def commit_user(self):
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'session_token': self.session_token,
            'authored_emotes': [emote.to_dict() for emote in self.authored_emotes],  # noqa
            'emotes': [emote.to_dict() for emote in self.emotes],
            'totem_skins': [skin.to_dict() for skin in self.totem_skins],
            'followed_totems': [totem.to_dict() for totem in self.followed_totems]  # noqa
        }
