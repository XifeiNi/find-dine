import enum
import sys
import os

from flask import Flask, jsonify
from flask_login import LoginManager, login_user
from flask_socketio import SocketIO

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))
from backend.Classes.message_system import Message_System
from backend.server.models import Conversation, Messages, User_Profile, Match, Right_Swipe, Business_Profile, Deals, db
from datetime import datetime, date

from backend.Classes.deals import Deals_system
from backend.Classes.reservations import Reservation_system

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'user_side#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
db.init_app(app)
socketio = SocketIO(app)

message_sys = Message_System()
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


class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3


class Gender_Preference(enum.Enum):
    male = 1
    female = 2
    everyone = 3


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


def view_profile():
    cu = current_user.get_cu()
    response = {'f_name': cu.f_name, 'l_name': cu.l_name,
                'email_address': cu.email_address, 'username': cu.username,
                'gender': str(cu.gender), 'gender_preference': str(cu.gender_preference),
                'max_match_distance': cu.max_match_distance, 'min_match_age': cu.min_match_age,
                'max_match_age': cu.max_match_age, 'bio': cu.bio}

    return response


def update_gender_preference(preference):
    cu = current_user.get_cu()
    if cu.gender_preference == preference:
        print("update_gender_preference: preference already assigned")
        return
    else:
        if preference == "male":
            cu.gender_preference = Gender_Preference.male
        if preference == "female":
            cu.gender_preference = Gender_Preference.female
        if preference == "everyone":
            cu.gender_preference = Gender_Preference.everyone
            db.session.commit()
        print("successfully updated gender preference")

    return

def update_min_match_age(age):
    cu = current_user.get_cu()
    age = int(age)
    print("age = ")
    print(age)
    if age < 16:
        print("no users are under 16 years of age")
        return
    if age > cu.max_match_age:
        print("min match age must be less than max match age")
        return
    cu.min_match_age = age
    print("successfully updated min match age")
    db.session.commit()
    return

def update_max_match_age(age):
    cu = current_user.get_cu()
    age = int(age)
    if age > 150:
        print("no-one is that old!")
        return
    if age > cu.max_match_age:
        print("max match age must be greater than min match age")
        return
    cu.max_match_age = age
    db.session.commit()
    print("successfully updated max match age")
    return

def update_max_match_distance(dist):
    cu = current_user.get_cu()
    dist = int(dist)
    if dist < 0:
        print("distance must be positive")
        return
    cu.max_match_distance = dist
    db.session.commit()
    print("successfully updated max match distance")
    return

def update_bio(new):
    if len(new) > 150:
        print("bio must be less than 150 characters")
        return
    current_user.get_cu().bio = new
    db.session.commit()
    print("successfully updated bio")
    return


def view_blocked():
    current_user_id = current_user.get_cu().id
    conversations = message_sys.getConversations(current_user_id)
    blocked_usernames = []
    for conversation in conversations:

        other_user_id = User_Profile.query.filter_by(id=conversation['username']).id

        # find match object
        match = Match.query.filter_by(first_swiper=other_user_id).first()
        if match is None:
            match = Match.query.filter_by(second_swiper=other_user_id).first()

        if match.blocked_by == current_user_id:
            if match.first_swiper != current_user_id:
                blocked_usernames.append(match.first_swiper.username)
            else:
                blocked_usernames.append(match.second_swiper.username)

    return blocked_usernames


def view_blockable():
    current_user_id = current_user.get_cu().id
    conversations = message_sys.getConversations(current_user_id)
    blockable = []
    for conversation in conversations:
        other_user_id = User_Profile.query.filter_by(id=conversation['username']).id

        ther_user_id = User_Profile.query.filter_by(id=conversation['username']).id

        # find match object
        match = Match.query.filter_by(first_swiper=other_user_id).first()
        if match is None:
            match = Match.query.filter_by(second_swiper=other_user_id).first()

        if match.blocked_by is not None:
            if match.first_swiper != current_user_id:
                blockable.append(match.first_swiper.username)
            else:
                blockable.append(match.second_swiper.username)

    return blockable


if __name__ == '__main__':
    pass
