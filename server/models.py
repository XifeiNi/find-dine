from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime, date
import enum


# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(64), unique=True, index=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     password = db.Column(db.String(128))
#     profile_settings = db.Column(db.Boolean, default = False)
#
#     events = db.relationship('Event')
#     # location = db.relationship('Location')
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))

class Conversation(db.Model):
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String)

    messages =db.relationship('Messages')


class Messages(db.Model):
    __tablename__ = 'messages'
    id= db.Column(db.Integer, primary_key=True)
    room=db.Column(db.String, db.ForeignKey('conversations.id'))
    sender_username = db.Column(db.String)
    time_sent = db.Column(db.Time)
    date_sent = db.Column(db.Date)
    message = db.Column(db.String)

class Business_Category(enum.Enum):
    1 = "Fine Dining"
    2 = "Casual Dining"

class Business_Profile(db.Model):
    __tablename__ = 'business_profile'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    email_address = db.Column(db.String)
    #main_profile_pic= not too sure how to link this to image in the db
    description = db.Column(db.String)
    address = db.Column(db.String)
    #menu = Not sure how to add an image 
    price_guide=db.Column(db.Integer)
    category=db.Column(db.Enum(Business_Category))

class Business_Offer(db.Model):
    __tablename__ = 'business_offer'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    description = db.Column(db.String)
    original_price = db.Column(db.Numeric(10,2))
    n_upcoming = db.Column(db.Integer)
    date_created = db.Column(db.Date)
    date_expiry = db.Column(db.Date)
    business=db.Column(db.Integer, db.ForeignKey('business_profile.id')) # not sure if this is accurate 



# class Location (db.Model): #Invitation System
#     __tablename__ = 'location'
#
#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     default_location = db.Column(db.String(128), default="")