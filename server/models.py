import flask_loginmanager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
import enum
from flask import current_app
from flask_login import UserMixin
from datetime import datetime, date

db = SQLAlchemy()
from datetime import datetime, date

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

# class Location (db.Model): #Invitation System
#     __tablename__ = 'location'
#
#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     default_location = db.Column(db.String(128), default="")

class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3


class Gender_Preference(enum.Enum):
    male = 1
    female = 2
    everyone = 3


class User_Profile(db.Model):
    __tablename__ = "user_profiles"
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(20))
    l_name = db.Column(db.String(20))
    email_address = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.Enum(Gender))
    gender_preference = db.Column(db.Enum(Gender_Preference))
    max_match_distance = db.Column(db.Integer)
    min_match_age = db.Column(db.Integer)
    max_match_age = db.Column(db.Integer)
    bio = db.Column(db.String(150))
    location = db.Column(db.String)
    # main_profile_pic = db.Image()??
    dob = db.Column(db.Date)  # change this later

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User_Profile.query.get(data['id'])
        return user