from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

from serv.models.location import Location
from serv.models.user import User
from serv import app, db


load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='blah', longitude=36.132725, latitude=-86.830465,
                 email='blah@blah.com',
                 password='password')
    user2 = User(username='blahan', longitude=36.1328855, latitude=-86.8302365,
                 email='oink@oink.com',
                 password='password')
    user3 = User(username='thatbl', longitude=139.839478, latitude=35.652832,
                 email='yeah@yeah.com',
                 password='password')
    user4 = User(username='hawaiib', longitude=-155.844437, latitude=19.741755,
                 email='no@no.com',
                 password='password')

    location1 = Location(longitude=36.132725, latitude=-86.830465)
    location2 = Location(longitude=36.1328855, latitude=-86.8302365)
    location3 = Location(longitude=36.1320190, latitude=-86.8324051)
    location4 = Location(longitude=139.839478, latitude=35.652832)

    location1.update_geo()
    location2.update_geo()
    location3.update_geo()
    location4.update_geo()

    user1.update_geo()
    user2.update_geo()
    user3.update_geo()
    user4.update_geo()

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)
    db.session.add(location4)
    db.session.commit()
