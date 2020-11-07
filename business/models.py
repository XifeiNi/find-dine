from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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
    category = db.Column(db.String)

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