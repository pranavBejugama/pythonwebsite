from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model): #layout or blueprint for an object thats goign to be stored in the database.
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key is a unique identifier, typically an integer that represents the object in the database. Ex. if someone had the same name, there needs to be some sort of differentiation.
    email = db.Column(db.String(150), unique=True) #no user can have the same email as other users
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

