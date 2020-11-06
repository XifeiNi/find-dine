from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import Business_Profile, db
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
        return render_template('login.html')

    return render_template('signup.html')

@app.route('/deal', methods=['GET', 'POST'])
def create_deal():
    if request.method == 'POST':
        data = request.form


if __name__ == '__main__':
    socketio.run(app, debug=True)
