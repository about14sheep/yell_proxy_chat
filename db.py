from dotenv import load_dotenv

from serv.models import User
from serv import app, db


load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='blah')
    user2 = User(username='blahandblah')
    user3 = User(username='thatblahblah')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
