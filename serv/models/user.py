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
    def get_all_users(cls):
        users = cls.query.all()
        return {'users': [user.to_dict() for user in users]}

    @classmethod
    def get_user_by_id(cls, id):
        user = cls.query.get(id)
        return {'user': user.to_dict()}

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
            'authored_emotes': [{
                                 'id': emote.id,
                                 'image_url': emote.image_url
                                 } for emote in self.authored_emotes],
            'emotes': [{
                        'id': emote.id,
                        'image_url': emote.image_url
                        } for emote in self.emotes],
            'totem_skins': [{
                             'id': skin.id,
                             'image_url': skin.image_url
                             } for skin in self.totem_skins],
            'followed_totems': [{
                                 'id': totem.id,
                                 'totem_skin_id': totem.totem_skin_id
                                 } for totem in self.followed_totems]
        }
