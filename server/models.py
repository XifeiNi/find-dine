from typing import List

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, abort
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

    messages = db.relationship('Messages')


class Messages(db.Model):
    __tablename__ = 'messages'
    id= db.Column(db.Integer, primary_key=True)
    room=db.Column(db.String, db.ForeignKey('conversations.id'))
    sender_username = db.Column(db.String)
    time_sent = db.Column(db.Time)
    date_sent = db.Column(db.Date)
    message = db.Column(db.String)

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
    #category=db.Column(db.Enum(Business_Category))
    deals = db.relationship('Deals')

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
                "business_id" : item[1],
                "deal_name": item[2],
                "description": item[3],
                "discount_percentage": item[4],
                "date_created": item[5],
                "date_expiry": item[6]
                #"date_created": datetime.date.strptime(item[6], "%d %b %Y")
            })

    return result

def deals_info(business_id):

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