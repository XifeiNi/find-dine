from flask import Flask, render_template, request, url_for, redirect, Response
from flask_socketio import SocketIO, join_room
import json
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
    if request.method == 'POST':
        data = request.form
        user_email = data['username']
        password = data['password']
        user = Business_Profile.query.filter_by(email=user_email).first()
        if user is not None and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Incorrect username/password")
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    all_deals = Deal.query.all()
    for deal in all_deals:
        if deal.date_expiry < date.today():
            db.session.delete(deal)
            db.session.commit()
    business_deals = Deal.query.filter_by(business_id=current_user.id).all()
    business = Business_Profile.query.filter_by(id=current_user.id).first()
    deals_frontend = []
    for deal in business_deals:
        deal_expiry = date.strftime(deal.date_expiry, '%d/%m/%Y')
        deal_created = date.strftime(deal.date_created, '%d/%m/%Y')
        business_deal = {"deal_id": deal.id,
                        "business_name":business.name,
                        "deal_name": deal.deal_name,
                        "description": deal.description,
                        "discount":deal.discount_percentage,
                        "expiry":deal_expiry,
                        "created":deal_created}
        deals_frontend.append(business_deal)

    return render_template('homepage.html', deals_frontend=deals_frontend, business_name=business.name)


@app.route('/delete_deal', methods=['POST'])
@login_required
def delete_deal():
    content = request.get_json()
    deal_id = content.get('deal_id')
    print ("*************************")
    id = int(deal_id)
    print (id)
    deal = Deal.query.filter_by(id=id).first()
    if deal is None:
        response_content = {
            'message': "Deal Not Found! Something is wrong"
        }
        return Response(json.dumps(response_content), mimetype='application/json')
    db.session.delete(deal)
    db.session.commit()
    response_content = {
        'message': "Deal was successfully deleted"
    }
    return Response(json.dumps(response_content), mimetype='application/json')

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
        print (created)
        created_datetime = datetime.strptime(created, '%Y-%m-%d')
        created_date = created_datetime.date()
        print (type(created_date))
        expiry_datetime = datetime.strptime(expiry, '%Y-%m-%d')
        expiry_date = expiry_datetime.date()
        print (type(expiry_date))
        deal = Deal(business_id=current_user.id,
                    deal_name=deal_name,
                    description=description,
                    discount_percentage=discount,
                    date_expiry=expiry_date,
                    date_created=created_date)
        db.session.add(deal)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_deal.html')
@app.route('/edit_deal', methods=['EDIT', 'POST'])
def edit_deal():
    print("In edit deal function")
    content = request.get_json()
    deal_id = content.get('deal_id')
    default_deal = Deal.query.filter_by(id=deal_id).first()
    if request.method == 'POST':
        data = request.form
        deal_name = data['deal_name']
        description = data['description']
        discount = data['percentage']
        expiry = data['expiry']
        created = data['created_date']
        print (created)
        created_datetime = datetime.strptime(created, '%Y-%m-%d')
        created_date = created_datetime.date()
        print (type(created_date))
        expiry_datetime = datetime.strptime(expiry, '%Y-%m-%d')
        expiry_date = expiry_datetime.date()
        print (type(expiry_date))
        if default_deal.deal_name != deal_name:
            new_deal_name = deal_name
        else:
            new_deal_name = default_deal.deal_name
        if default_deal.description != description:
            new_description = description
        else:
            new_description = default_deal.description
        if default_deal.discount != discount:
            new_discount = discount
        else:
            new_discount = default_deal.discount
        if default_deal.date_expiry != expiry:
            new_expiry = expiry
        else:
            new_expiry = default_deal.date_expiry
        if default_deal.date_created != created_date:
            new_created_date = created_date
        else:
            new_created_date = default_deal.date_created
        default_deal.deal_name = new_deal_name
        default_deal.description = new_description
        default_deal.discount = new_discount
        default_deal.date_expiry = new_expiry
        default_deal.date_created = new_created_date
        db.session.commit()
        return  redirect(url_for('home'))
    return render_template('edit_deal.html')

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
