from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

from serv.models.emote import Emote
from serv.models.bot import Bot
from serv.models.totem_skin import Totem_Skin
from serv.models.totem import Totem
from serv.models.user import User
from serv import app, db


load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='blah', email='balh@blah.com',
                 hashed_password=generate_password_hash('password'))
    user2 = User(username='lee', email='lee@lee.com',
                 hashed_password=generate_password_hash('password'))
    user3 = User(username='fattony', email='fattony@fattony.com',
                 hashed_password=generate_password_hash('password'))

    bot1 = Bot(name='yellbot', bot_key='gjbnraskguba')
    bot2 = Bot(name='demobot', bot_key='ogwrnboiwrgbbo')
    bot3 = Bot(name='fembot', bot_key='kkfkfkfkfk')

    emote1 = Emote(image_url='fatbopi.jpeg', author_id=3)
    emote2 = Emote(image_url='smallboi.jpeg', author_id=3)
    emote3 = Emote(image_url='mediumboi.jpeg', author_id=1)

    totem_skin1 = Totem_Skin(image_url='totemboi.png')
    totem_skin2 = Totem_Skin(image_url='soapbox.jpeg')
    totem_skin3 = Totem_Skin(image_url='baseskin.jpeg')

    totem1 = Totem(user_id=1, totem_skin_id=3)
    totem2 = Totem(user_id=2, totem_skin_id=1)
    totem3 = Totem(user_id=3, totem_skin_id=2)

    totem1.bots.append(bot1)
    totem1.bots.append(bot2)
    totem1.followers.append(user1)
    totem1.followers.append(user2)
    totem1.followers.append(user3)

    totem2.bots.append(bot1)
    totem2.followers.append(user1)

    totem3.bots.append(bot1)
    totem3.bots.append(bot2)
    totem3.bots.append(bot3)
    totem3.followers.append(user1)
    totem3.followers.append(user2)
    totem3.followers.append(user3)

    user1.emotes.append(emote1)
    user1.emotes.append(emote2)
    user1.emotes.append(emote3)
    user1.totem_skins.append(totem_skin1)
    user1.totem_skins.append(totem_skin2)
    user1.totem_skins.append(totem_skin3)

    user2.emotes.append(emote1)
    user2.emotes.append(emote2)
    user2.emotes.append(emote3)
    user2.totem_skins.append(totem_skin1)
    user2.totem_skins.append(totem_skin2)
    user2.totem_skins.append(totem_skin3)

    user3.emotes.append(emote1)
    user3.emotes.append(emote2)
    user3.emotes.append(emote3)
    user3.totem_skins.append(totem_skin1)
    user3.totem_skins.append(totem_skin2)
    user3.totem_skins.append(totem_skin3)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.add(bot1)
    db.session.add(bot2)
    db.session.add(bot3)

    db.session.add(totem1)
    db.session.add(totem2)
    db.session.add(totem3)

    db.session.add(emote1)
    db.session.add(emote2)
    db.session.add(emote3)

    db.session.add(totem_skin1)
    db.session.add(totem_skin2)
    db.session.add(totem_skin3)

    db.session.commit()
