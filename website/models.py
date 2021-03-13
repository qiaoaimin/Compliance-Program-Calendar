from .exts import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(50))


#    programs = db.relationship('Program')


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(1000))
    frequency = db.Column(db.Integer)
    participants_No = db.Column(db.Integer)
    participants_group = db.Column(db.String(150))
    duration = db.Column(db.Integer)
    status = db.Column(db.String(50))
    hold_date = db.Column(db.DateTime())
    created_data = db.Column(db.DateTime(timezone=True), default=func.now())
    created_by = db.Column(db.String(50), db.ForeignKey('user.id'))


class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
