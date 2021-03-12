from flask import Flask, Blueprint
from . import configs
from .exts import db, create_database
from .models import User, Program, Attendee
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    create_database(app)

    return app
