import sys
import os

from flask import Flask
from flask_login import LoginManager, login_user
from flask_socketio import SocketIO

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))
from backend.server.models import Conversation, Messages, User_Profile, Match, Right_Swipe, Business_Profile, Deals, db
from datetime import datetime, date

from backend.Classes.deals import Deals_system
from backend.Classes.reservations import Reservation_system

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'user_side#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
db.init_app(app)
socketio = SocketIO(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User_Profile.query.filter_by(id=user_id).first()

with app.app_context():
    db.create_all()
    db.session.expire_on_commit = False


class CurrentUser:
    cu = None

    def set_cu(self, curr):
        self.cu = curr

    def get_cu(self):
        return self.cu


current_user = CurrentUser()


def signup(request):
    req = request
    print(req)

    # get data from form
    email = req['email']
    username = req['username']
    f_name = req['f_name']
    l_name = req['l_name']
    input_password = req['password']
    input_password_repeat = req['password_repeat']
    dob = req['dob']
    min_target = req['min_target']
    max_target = req['max_target']
    gender = req['gender']
    gender_preference = req['gender_preference']
    bio = req['bio']
    location = req['location']
    max_match_distance = req['max_match_distance']

    # do validation and error checking
    if User_Profile.query.filter_by(email_address=email).first() is not None:
        print("signup: error: An account with this email already exists")
        return

    if User_Profile.query.filter_by(username=username).first() is not None:
        print("signup: error: Username already taken")
        return

    if input_password != input_password_repeat:
        print("signup: error: Passwords don't match")
        return

    if min_target > max_target:
        print("signup: error: Invalid match age targets")
        return

    dob_obj = datetime.strptime(dob, '%Y-%m-%d')
    if datetime.today().year - dob_obj.year < 16:
        print("signup: error: You must be over 16 to register on find&dine")
        return

    # create object and commit to db
    new_user = User_Profile(f_name=f_name,
                            l_name=l_name,
                            email_address=email,
                            username=username,
                            password_hash=input_password,
                            gender=gender,
                            gender_preference=gender_preference,
                            min_match_age=min_target,
                            max_match_age=max_target,
                            bio=bio,
                            dob=dob_obj,
                            location=location,
                            max_match_distance=max_match_distance)

    db.session.add(new_user)
    db.session.commit()

    # redirect to home page, user is logged in
    new_user.is_authenticated = True
    current_user.set_cu(new_user)

    print("new user created successfully!")
    return


def login(request):
    req = request

    username = req['username']
    password = req['password']

    # validation
    user = User_Profile.query.filter_by(username=username).first()
    if user is None:
        print("login: error: invalid credentials")
        return

    if user.password_hash != password:
        print("login: error: invalid credentials")
        return

    # user is valid
    user.is_authenticated = True
    current_user.set_cu(user)
    print("successfully logged in!")

    return


def logout():
    current_user.is_authenticated = False
    current_user.set_cu(None)

    print("successfully logged out!")

    return


if __name__ == '__main__':
    pass
