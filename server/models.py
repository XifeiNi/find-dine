
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

class Match(db.Model):
    __tablename__ = 'match'

    id=db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    first_swiper = db.Column(db.Integer, db.ForeignKey("user_profiles.id"))
    second_swiper = db.Column(db.Integer)
    conversation_id = db.Column(db.String, db.ForeignKey("conversations.room"))

class Right_Swipe(db.Model):
    __tablename__ = 'right_swipe'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    swiper_id = db.Column(db.Integer, db.ForeignKey("user_profiles.id"))
    target_id = db.Column(db.Integer)
    became_match = db.Column(db.Boolean, default=False)


class Conversation(db.Model):
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String, unique=True)
    username_one=db.Column(db.Integer, db.ForeignKey("user_profiles.id"))
    username_two=db.Column(db.Integer)

    messages =db.relationship('Messages')
    matches = db.relationship('Match')


class Messages(db.Model):
    __tablename__ = 'messages'
    id= db.Column(db.Integer, primary_key=True)
    room=db.Column(db.String, db.ForeignKey('conversations.room'))
    sender_username = db.Column(db.Integer, db.ForeignKey("user_profiles.id"))
    time_sent = db.Column(db.DateTime)
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
    right_swipes = db.relationship('Right_Swipe')
    conversations = db.relationship('Conversation')
    messages = db.relationship("Messages")
    users = db.relationship("Match")
    # main_profile_pic = db.Image()??
    dob = db.Column(db.Date)

    # flask login manager requirements
    is_authenticated = False
    is_active = True
    is_anonymous = False

    # return unicode id
    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")

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
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token

        user = User_Profile.query.get(data['id'])
        return user