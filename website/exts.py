from flask_sqlalchemy import SQLAlchemy
from os import path
from .configs import SITE_PATH, DB_NAME

db = SQLAlchemy()


def create_database(app):
    if not path.exists(SITE_PATH + '/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created!')
