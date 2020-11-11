import json
from typing import List
import flask_loginmanager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
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
    time_start = db.Column(db.String)
    time_end = db.Column(db.String)


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
    all_matches = Match.query.filter(or_(Match.first_swiper == user_id, Match.second_swiper == user_id)).all()
    # print(all_matches)
    matched_users = []

    ''' right_swipe_1 = Right_Swipe(time=datetime.now(),
                swiper_id=user_id,
                target_id=1,
                became_match=False)

    right_swipe_2 = Right_Swipe(time=datetime.now(),
                swiper_id=1,
                target_id=user_id,
                became_match=True)

    db.session.add(right_swipe_1)
    db.session.add(right_swipe_2)
    db.session.commit()

    room_id = str(right_swipe_1.swiper_id) + "+" + str(right_swipe_1.target_id)

    conversation = Conversation(room=room_id,
                                username_one=right_swipe_1.swiper_id,
                                username_two=right_swipe_1.target_id)
    db.session.add(conversation)
    db.session.commit()

    match = Match(distance=12,
                  created=datetime.now(),
                  first_swiper=right_swipe_1.target_id,
                  second_swiper=right_swipe_1.swiper_id,
                  conversation_id=room_id)
    db.session.add(match)
    db.session.commit()'''

    # print(all_matches)
    # if (all_matches.len)
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


def generate_meeting_id():
    num = (Meeting.query.order_by(Meeting.id.desc()).first())
    if num is None:
        return 1
    else:
        new_id = num.id + 1


def add_meeting(deal_id, match_id, start_t, end_t):
    meeting_id = generate_meeting_id()
    result = []
    meeting = Meeting(
        id=meeting_id,
        deals_id=deal_id,
        match_id=match_id,
        time_start=str(start_t),
        time_end=str(end_t)
    )
    print(meeting.time_start)
    db.session.add(meeting)
    db.session.commit()
    result.append({
        "id": meeting_id,
        "deals_id": deal_id,
        "match_id": match_id,
        "time_start": start_t,
        "time_end": end_t,
    })
    #json_result = json.dumps(meeting.to_dict())
    return result


# class Location (db.Model): #Invitation System
#     __tablename__ = 'location'
#
#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     default_location = db.Column(db.String(128), default="")
