from flask import Flask, render_template
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import Business_Profile, db
from datetime import datetime, date

app = Flask(__name__, template_folder='/templates')
app.config['SECRET_KEY'] = 'business_side'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
socketio = SocketIO(app)

with app.app_context():
    db.create_all()
@app.route('/signup', methods=['POST'])
def signup(data):
    name = data['name']
    email_address = data['email']
    password = data['password']
    description = data['description']
    address = data['address']
    price_guide = data['price']
    category = data['category']

    business = Business_Profile()
if __name__ == '__main__':
    socketio.run(app, debug=True)
