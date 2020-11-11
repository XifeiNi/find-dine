from typing import List
import flask_loginmanager
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, abort

db = SQLAlchemy()
from flask import current_app
from flask_login import UserMixin
from datetime import datetime, date
import enum
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

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


'''class Business_Category(enum.Enum):
    one = "Fine Dining"
    two = "Casual Dining"'''


class Business_Profile(db.Model):
    __tablename__ = 'business_profile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    # main_profile = db.Column(db)
    description = db.Column(db.String)
    address = db.Column(db.String)
    # menu = db.Column
    price_guide = db.Column(db.String)
    category = db.Column(db.String)
    # category=db.Column(db.Enum(Business_Category))
    deals = db.relationship('Deals')


class Meeting(db.Model):
    __tablename__ = "meeting"

    id = db.Column(db.Integer, primary_key=True)
    deals_id = db.Column(db.Integer, db.ForeignKey('deals.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    time_start = db.Column(db.Date)
    time_end = db.Column(db.Date)


class Deals(db.Model):
    __tablename__ = 'deals'

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business_profile.id'))
    deal_name = db.Column(db.String)
    description = db.Column(db.String)
    original_price = db.Column(db.Integer)
    discount_percentage = db.Column(db.Integer)
    date_expiry = db.Column(db.Date)
    date_created = db.Column(db.Date)


# company = relationship("Company", foreign_keys=[company_id])

class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
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
    username_one = db.Column(db.Integer, db.ForeignKey("user_profiles.id"))
    username_two = db.Column(db.Integer)
    messages = db.relationship('Messages')
    matches = db.relationship('Match')


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String, db.ForeignKey('conversations.room'))
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
    dob = db.Column(db.Date)  # change this later

    right_swipes = db.relationship('Right_Swipe')
    conversations = db.relationship('Conversation')
    messages = db.relationship("Messages")
    users = db.relationship("Match")


def all_businesses_list():
    import csv
    with open('Business_Profile.csv', newline='') as csvfile:
        businesses_list = csv.reader(csvfile, delimiter='\n', quotechar='|')
        result = []
        for row in businesses_list:
            item: List[str] = row[0].split(',')
            result.append({
                "id": int(item[0]),
                "name": item[1],
                "email": item[2],
                "description": item[3],
                "address": item[4],
                "price_guide": item[5],
                "category": item[6]
            })

    return result


def all_deals_list():
    import csv
    with open('Deal.csv', newline='') as csvfile:
        deals_list = csv.reader(csvfile, delimiter='\n', quotechar='|')
        result = []
        for row in deals_list:
            item: List[str] = row[0].split(',')
            result.append({
                "id": int(item[0]),
                "business_id": item[1],
                "deal_name": item[2],
                "description": item[3],
                "discount_percentage": item[4],
                "date_created": item[5],
                "date_expiry": item[6]
                # "date_created": datetime.date.strptime(item[6], "%d %b %Y")
            })

    return result


def deals_info(business_id):
    return


def get_matched_users(user_id):
    all_matches = Match.query.filter(or_(first_swiper=user_id, second_swiper=user_id)).all
    matched_users = []

    for match in all_matches:

        if match.first_swiper == user_id:
            user = User_Profile.query.filter_by(id=match.second_swiper).first()
            name = user.f_name + " " + user.l_name
            matched_users.append({
                "user_id": user.id,
                "match_id": match.id,
                "user_name": name
            })
        if match.second_swiper == user_id:
            user = User_Profile.query.filter_by(id=match.first_swiper).first()
            name = user.f_name + " " + user.l_name
            matched_users.append({
                "id": user.id,
                "match_id": match.id,
                "user_name": name
            })

    return matched_users

    '''
	# get patient info
	sql = """
		select p.cancer_type, p.diagnosis
		from Patient p 
		where p.patient_id = '{}'
	""".format(patient_id)

	cursor.execute(sql)
	patient = cursor.fetchone()
	if patient is None:
		return 400

	# get patient current treatment
	sql = """
		select group_concat(treatment) as treatments
		from Treatment_start
		where event_id in 
			(select event_id
			from Event 
			where patient_id = '{}' and type = "Treatment_start")
		and end_id is null;
	""".format(patient_id)
	cursor.execute(sql)
	current_treatment = cursor.fetchone()

	if current_treatment[0] is None:
		treatment = []
	else:
		treatment = current_treatment[0].split(",")

	result = {
		"ID": patient_id,
		"cancer_type": patient[0],
		"diagnosis": patient[1],
		"treatments": treatment,
		"events": get_events(patient_id),
		"status": 200
	}

	return result'''

# class Location (db.Model): #Invitation System
#     __tablename__ = 'location'
#
#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     default_location = db.Column(db.String(128), default="")
