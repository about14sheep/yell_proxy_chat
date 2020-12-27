from dotenv import load_dotenv

from serv.models import User, Location
from serv import app, db


load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='blah')
    user2 = User(username='blahandblah')
    user3 = User(username='thatblahblah')

    location1 = Location(longitude=36.132725, latitude=-86.830465)
    location2 = Location(longitude=36.1328855, latitude=-86.8302365)
    location3 = Location(longitude=36.1320190, latitude=-86.8324051)

    location1.update_geo()
    location2.update_geo()
    location3.update_geo()

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)
    db.session.commit()
