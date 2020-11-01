from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import Business_Profile, db
from datetime import datetime, date

app = Flask(__name__, template_folder='/business')
app.config['SECRET_KEY'] = 'business_side'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
socketio = SocketIO(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form['signup_form']
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
        db.commit()
        return render_template('business/signup.html')

    return render_template('business/signup.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
