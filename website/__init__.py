from flask import Flask, Blueprint
from . import configs
from .exts import db, create_database
from .models import User, Program, Attendee
from .views import views
from .auth import auth
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app
