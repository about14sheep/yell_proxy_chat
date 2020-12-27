from .models import db
from .config import Config

from .api.user_routes import user_routes
from .api.location_routes import location_routes

import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(location_routes, url_prefix='/api/locations')
