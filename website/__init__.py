from flask import Flask
from . import configs
from .exts import db, create_database
from .models import User, Program, Attendee


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    db.init_app(app)

    create_database(app)

    return app
