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

    messages =db.relationship('Deal')


# class Deal(db.Model):
#     __tablename__ = 'messages'
#     id= db.Column(db.Integer, primary_key=True)
#     room=db.Column(db.String, db.ForeignKey('conversations.id'))
#     sender_username = db.Column(db.String)
#     time_sent = db.Column(db.Time)
#     date_sent = db.Column(db.Date)
#     message = db.Column(db.String)