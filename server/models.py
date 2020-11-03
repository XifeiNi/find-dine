from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from app import app
import enum

db = SQLAlchemy(app)

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
    email_address = db.Colomn(db.String(50), unique=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.Enum(Gender))
    gender_preference = db.Column(db.Enum(Gender_Preference))
    max_match_distance = db.Column(db.Integer)
    min_match_age = db.Column(db.Integer)
    max_match_age = db.Column(db.Integer)
    bio = db.Column(db.String(150))
    # main_profile_pic = db.Image()??
    dob = db.Column(db.Date) #change this later
    

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