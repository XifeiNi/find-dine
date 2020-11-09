from flask_sqlalchemy import SQLAlchemy
import enum
db = SQLAlchemy()

class Business_Category(enum.Enum):
    one = "Fine Dining"
    two = "Casual Dining"

class Business_Profile(db.Model):
    __tablename__ = 'business_profile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    # main_profile = db.Column(db)
    description = db.Column(db.String)
    address = db.Column(db.String)
    # menu = db.Column
    price_guide = db.Column(db.String)
    category=db.Column(db.Enum(Business_Category))

class Deal(db.Model):
    __tablename__ = 'deal'
    id = db.Column(db.Integer, primary_key=True)
    deal_name = db.Column(db.String)
    description = db.Column(db.String)
    # deal_image = db.Column(db.)
    # original_price = db.Column(db.Integer)
    discount_percentage = db.Column(db.Integer)
    date_expiry = db.Column(db.Date)
    date_created = db.Column(db.Date)


'''class Business_Profile(db.Model):
    __tablename__ = 'businegss_profile'
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

class Offer_Time(db.Model):
    __tablename__ = 'offer_time'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time_start = db.Column(db.Time)
    time_end = db.Column(db.Time)
    offer=db.Column(db.Integer, db.ForeignKey('business_offer.id')) # not sure if this is accurate '''



# class Deal(db.Model):
#     __tablename__ = 'messages'
#     id= db.Column(db.Integer, primary_key=True)
#     room=db.Column(db.String, db.ForeignKey('conversations.id'))
#     sender_username = db.Column(db.String)
#     time_sent = db.Column(db.Time)
#     date_sent = db.Column(db.Date)
#     message = db.Column(db.String)

