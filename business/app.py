from flask import Flask, render_template, request, url_for, redirect, current_app
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import Business_Profile, Deal, db
from flask_login import current_user, login_user, login_required, logout_user
from datetime import datetime, date

app = Flask(__name__, template_folder='../templates/business')
app.config['SECRET_KEY'] = 'business_side'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
socketio = SocketIO(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print("I am in here")
        data = request.form
        print ("I got data")
        print (data)
        name = data['business_name']
        email_address = data['email']
        password = data['password']
        description = data['description']
        address = data['address']
        price_guide = data['price_guide']
        category = data['category']
        business = Business_Profile(name=name,
                                    email=email_address,
                                    password=password,
                                    description=description,
                                    address=address,
                                    price_guide=price_guide,
                                    category=category)
        db.session.add(business)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         data = request.form
#         user_email = data['username']
#         password = data['password']
#         user = Business_Profile.query.filter_by(email=user_email).first()
#         if user is not None and user.password == password:
#             login_user(user, login_form.remember_me.data)
#             return redirect(url_for('main.dashboard'))
#     return render_template('login.html')
@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/deal', methods=['GET', 'POST'])
def create_deal():
    if request.method == 'POST':
        data = request.form
        deal_name = data['deal_name']
        description = data['description']
        discount = data['percentage']
        expiry = data['expiry']
        created = data['created_date']
        deal = Deal(deal_name=deal_name,
                    description=description,
                    discount_percentage=discount,
                    date_expiry=expiry,
                    date_created=created)
        db.session.add(deal)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_deal.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
