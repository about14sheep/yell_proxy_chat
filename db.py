from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

from serv.models.emote import Emote
from serv.models.bot import Bot
from serv.models.location import Location
from serv.models.totem_skin import Totem_Skin
from serv.models.totem import Totem
from serv.models.user import User
from serv import app, db


load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()
