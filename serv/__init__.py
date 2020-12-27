from .models import db
from .config import Config
import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
