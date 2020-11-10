from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import Business_Profile, Deal, db
from flask_login import current_user, login_user, login_required, logout_user, LoginManager
from datetime import datetime, date

app = Flask(__name__, template_folder='../templates/business')
login = LoginManager(app)

@login.user_loader
def load_user(id):
    return Business_Profile.query.get(int(id))


app.config['SECRET_KEY'] = 'business_side'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
socketio = SocketIO(app)

with app.app_context():
    db.create_all()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print("I am in here")
        data = request.form
        print ("I got data")
        print (data)
        name = data['business_name']
        email_address = data['email']
        password = data['password']
        contact = data['contact_number']
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
                                    phone_number=contact,
                                    category=category)
        db.session.add(business)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        data = request.form
        user_email = data['username']
        password = data['password']
        user = Business_Profile.query.filter_by(email=user_email).first()
        if user is not None and user.password == password:
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Incorrect username/password")
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    business_deals = Deal.query.filter_by(business_id=current_user.id).all()
    business = Business_Profile(id=current_user.id).first()
    deals_frontend = []
    for deal in business_deals:
        business_deal = {"business_name":business.name,
                        "deal_name": deal.name,
                        "description": deal.description,
                        "discount":deal.discount_percentage,
                        "expiry":deal.date_expiry,
                        "created":deal.date_created}
        deals_frontend.append(business_deal)

    return render_template('homepage.html', deals_frontend=deals_frontend, business_name=business.name)

@app.route('/deal', methods=['GET', 'POST'])
@login_required
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

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        data = request.form
        user_email = data['email']
        password = data['password']
        user = Business_Profile.query.filter_by(email=user_email).first()
        if user is not None:
            user.password = password
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('forgot_password.html', error="Username does not exist! Please signup!")
    return render_template('forgot_password.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
