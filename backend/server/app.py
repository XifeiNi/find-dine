# from flask import Flask, render_template, session
# from flask_socketio import SocketIO, send, emit, join_room, leave_room
#
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
#
# # @app.route('/login')
# # def login():
# #     check password - assuming thats fine
# #     session['user'] = database.get("username")
#
# @app.route('/')
# def startup():
#     return """
#      <!DOCTYPE html>
#     <script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
# <script type="text/javascript" charset="utf-8">
#     var socket = io();
#     socket.on('connect', function() {
#         socket.emit('join', {username: 'You\\'re fucked''});
#     });
# </script>
#     """
#
# # @app.route('/logout')
# # def logout():
# #     session.clear()
#
# @socketio.on('connect')
# def handle_message():
#     print('someone connected')
#
# @socketio.on('message')
# def handle_message(message):
#     room = session['room']
#     send(message, room=room)
#
# @socketio.on('join')
# def on_join(data):
#     # username = session['user'].get('username')
#     # room = username + data['other']
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     session['room'] = room
#     send('Oi dickhead, join this room ' + room)
#     send(username + ' has entered the room.', room=room)
#     send('blah', room='qwer')
#     emit('message', 'blah', room='qwer')
#
# @socketio.on('leave')
# def on_leave(data):
#     # username = session['user'].get('username')
#     # room = username + data['other']
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)
#
# if __name__ == '__main__':
#     socketio.run(app)
import sys
import os

import flask
from werkzeug.urls import url_parse

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from flask import Flask, render_template, session, jsonify, request, redirect, url_for, flash
from urllib.parse import urlparse, urljoin
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from backend.server.models import Conversation, Messages, User_Profile, Match, Right_Swipe, Business_Profile, Deals, db
from backend.Classes.recommendation_system import Recommendation_System, Right_Swipes
from backend.Classes.message_system import Message_System
from datetime import datetime, date

from backend.Classes.deals import Deals_system
from backend.Classes.reservations import Reservation_system

# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_jsglue import JSGlue
# from config import Config
#
# # Extension Initialisation
# bootstrap = Bootstrap()
# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# jsglue = JSGlue()
#
# # Factory Function
# def create_app():
#     # Create Flask Instance
#     app = Flask(__name__, static_url_path='/static')
#     app.config.from_object(Config)
#
#     # Apply Extension to Flask Instance
#     bootstrap.init_app(app)
#     db.init_app(app)
#     login_manager.init_app(app)
#     jsglue.init_app(app)

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'user_side#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
db.init_app(app)
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# needed for login manager implementation. Gets user object from id
@login_manager.user_loader
def load_user(user_id):
    return User_Profile.query.filter_by(id=user_id).first()


with app.app_context():
    db.create_all()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        req = request.form
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

        # do validation and error checking
        if User_Profile.query.filter_by(email_address=email).first() is not None:
            return render_template('auth/signup.html', error="An account with this email already exists")

        if User_Profile.query.filter_by(username=username).first() is not None:
            return render_template('auth/signup.html', error="Username already taken")

        if input_password != input_password_repeat:
            return render_template('auth/signup.html', error="Passwords don't match")

        if min_target > max_target:
            return render_template('auth/signup.html', error="Invalid match age targets")

        dob_obj = datetime.strptime(dob, '%Y-%m-%d')
        if datetime.today().year - dob_obj.year < 18:
            return render_template('auth/signup.html', error="You must be over 18 to register on find&dine")

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
                                dob=dob_obj)

        db.session.add(new_user)
        db.session.commit()

        # redirect to home page, user is logged in
        login_user(new_user)
        return redirect(url_for('get_recommendations'))

    return render_template('auth/signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        req = request.form
        print(req)

        username = req['username']
        password = req['password']

        # validation
        user = User_Profile.query.filter_by(username=username).first()
        if user is None:
            return render_template('auth/login.html', error="Invalid credentials")

        if user.password_hash != password:
            return render_template('auth/login.html', error="Invalid credentials")

        # user is valid
        login_user(user, remember=True)
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('get_recommendations'))

    return render_template('auth/login.html')


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    response = {'f_name': current_user.f_name, 'l_name': current_user.l_name,
                'email_address': current_user.email_address, 'username': current_user.username,
                'gender': str(current_user.gender), 'gender_preference': str(current_user.gender_preference),
                'max_match_distance': current_user.max_match_distance, 'min_match_age': current_user.min_match_age,
                'max_match_age': current_user.max_match_age, 'bio': current_user.bio}

    return jsonify(response)

@app.route('/profile/match_preferences', methods=['GET', 'POST'])
@login_required
def match_preferences():

    if request.method == 'POST':
        req = request.form
        current_user.gender_preference = req['gender_preference']
        current_user.min_match_age = req['min_match_age']
        current_user.max_match_age = req['max_match_age']
        current_user.max_match_distance = req['max_match_distance']

    response = {'gender_preference': str(current_user.gender_preference), 'min_match_age': current_user.min_match_age,
                'max_match_age': current_user.max_match_age, 'max_match_distance': current_user.max_match_distance}

    return jsonify(response)


# This is the first function, once called, it should return the match recommendations
@app.route('/recommendations')
@login_required
def get_recommendations():
    # def sessions(origin):

    origin = "Main Library, University of New South Wales, Sydney, Australia"
    recs_sys = Recommendation_System()
    # current_user_id = current_user.id
    current_user_id = current_user.id
    user = User_Profile.query.filter_by(id=current_user_id).first()
    user.location = origin
    db.session.commit()
    recommendations = recs_sys.getRecommendations(origin, current_user_id)
    print(len(recommendations))
    # To print during pytest, uncomment False Assertion
    for recommendation in recommendations:
        # event.user_id = owner.id
        print("########################")
        print("Username: ", recommendation['match_user_username'])
        print("Distance: ", recommendation['distance'])
    return jsonify(recommendations)
    # return render_template('index.html', recommendations=recommendations)


@app.route("/get_conversations")
@login_required
def get_conversations():
    message_sys = Message_System()
    conversations = message_sys.getConversations(current_user.id)
    for conversation in conversations:
        print("########################")
        # print("First Name: ", recommendation.f_name)
        # print ("Last Name: ", recommendation.l_name)
        # print("addr: ", event.addr)
        # print("start: ", event.start_time)
        # print("end: ", event.end_time)
        print("Username: ", conversation['username'])
        print("Last_Message: ", conversation['last_message'])
        print("Time: ", conversation['time'])
    return jsonify(conversations)
    # return render_template('conversations.html', conversations=conversations)


@app.route("/get_conversation_messages/<room_id>")
@login_required
# @login_required
def get_conversation_messages(room_id):
    message_sys = Message_System()
    conversation, messages = message_sys.getMessages(room_id, current_user.id)
    print("########################")
    print("Username: ", conversation['conversation_username'])
    print("***********************")
    for message in messages:
        print("Message Sender: ", message['message_username'])
        print("Message: ", message['message'])
        print("Time: ", message['time_sent'])
    return jsonify({'conversation': conversation, 'messages': messages})
    # return render_template('messages.html', conversation=conversation, messages=messages)


def messageReceived():
    print('message was received!!!')


# This message should be called when the user is trying to send a message, to an existing
# conversation
@socketio.on('send_message')
def handle_send_message(json):
    print('received my event: ' + str(json))
    current_user_id = current_user.id
    username = User_Profile.query.filter_by(username=json['user_name']).first()
    if username is None:
        socketio.emit('my response', json, callback="Something is wrong, Username cannot be found")
        exit(100)

    conversation = Conversation.query.filter_by(username_one=username.id).filter_by(
        username_two=current_user_id).first()
    if conversation is None:
        conversation = Conversation.query.filter_by(username_two=username.id).filter_by(
            username_one=current_user_id).first()
    if conversation is None:
        socketio.emit('my response', json, callback="Something is wrong, Conversation Room cannot be found")
        exit(200)
    room = conversation.room
    message = Messages(room=room,
                       sender_username=username.id,
                       time_sent=datetime.now(),
                       message=json['message'])
    db.session.add(message)
    db.session.commit()
    socketio.emit('my response', json, callback=messageReceived)


# This function should be called when the user right-swipes on an individual
@socketio.on('join')
def on_join(match_dict):
    right_swipes = Right_Swipes()
    current_user_id = current_user.id
    target_id = User_Profile.query.filter_by(username=match_dict['match_user_username']).first().id
    previous_swipe = right_swipes.right_swipes(match_dict, current_user_id, target_id)
    if previous_swipe == 1:
        second_right_swipe = Right_Swipe(time=datetime.now(),
                                         swiper_id=current_user_id,
                                         target_id=target_id,
                                         became_match=True)
        db.session.add(second_right_swipe)
        db.session.commit()
        room_id = str(target_id) + "+" + str(current_user_id)
        conversation = Conversation(room=room_id,
                                    username_one=target_id,
                                    username_two=current_user_id)
        db.session.add(conversation)
        db.session.commit()
        match = Match(distance=match_dict['distance'],
                      created=datetime.now(),
                      first_swiper=target_id,
                      second_swiper=current_user_id,
                      conversation_id=room_id)
        db.session.add(match)
        db.session.commit()
        found_match = {"succesful_error_message": "Found a match",
                       "successful_error_code": 0}
        code = found_match
        # socketio.emit("join_response", found_match)
    elif previous_swipe == -1:
        first_right_swipe = Right_Swipe(time=datetime.now(),
                                        swiper_id=current_user_id,
                                        target_id=target_id)
        db.session.add(first_right_swipe)
        db.session.commit()
        first_right_swipe = {"successful_error_message": "Request has been included into our system",
                             "successful_error_code": 1}
        code = first_right_swipe
        # socketio.emit("join_response", first_right_swipe)
    else:
        error_code = {"successful_error_message": "Something went wrong",
                      "successful_error_code": -1}
        code = error_code
    return code
    # socketio.emit("join_response", error_code)


@app.route('/businesses', methods=['GET', 'POST'])
def business_list():
    deals_sys = Deals_system()
    if request.method == 'GET':
        result = deals_sys.all_businesses_list()

        # return jsonify(result)
        return render_template('business_list.html', list=result)
    if request.method == 'POST':

        if request.form['submit_button'] == 'search_name':
            business_name = request.form['b_name']
            result = deals_sys.find_business_profile(business_name)
            return jsonify(result)

        if request.form['submit_button'] == 'search_category':
            business_category = request.form['category']
            print(business_category)
            result = deals_sys.sort_category(business_category)
            return jsonify(result)


@app.route('/deals', methods=['GET'])
# @login_required
def deals_list():
    if request.method == 'GET':
        deals_sys = Deals_system()
        result = deals_sys.all_deals_list()
        # return jsonify(result)
        return render_template('deals.html', list=result)


@app.route('/businesses/<b_id>', methods=['POST'])
def deals_filtered(b_id):
    if request.method == 'POST':
        deals_sys = Deals_system()
        result = deals_sys.deals_for_business(b_id)

        return jsonify(result)


@app.route('/deals/exp_sort', methods=['POST'])
def sort_by_expiry():
    if request.method == 'POST':
        deals_sys = Deals_system()
        result = deals_sys.sort_expiry()

        return jsonify(result)


@app.route('/reservation/<d_id>', methods=['POST'])
# @login_required
def make_reservation(d_id):
    if request.method == 'POST':

        reservations_sys = Reservation_system()

        if request.form['submit_button'] == 'reservation':
            deal_info = []
            current_user_id = current_user.id

            matched_users = reservations_sys.get_matched_users(current_user_id)

            deal = Deals.query.filter_by(id=d_id).first()

            business = Business_Profile.query.filter_by(id=deal.business_id).first()
            deal_info.append({
                "deal_id": deal.id,
                "deal_name": deal.deal_name,
                "deal_expiry": deal.date_expiry,
                "business_name": business.name,
                "business_address": business.address
            })
            return render_template('reservations.html', deal=deal_info, matches=matched_users)

        if request.form['submit_button'] == 'finalise_reservation':
            match_id = request.form.get('matched_user')
            date_of_meeting = request.form.get('date_of_meeting')
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')

            date_time_obj = datetime.strptime(date_of_meeting, '%Y-%m-%d')
            check = reservations_sys.check_date(d_id, date_time_obj.date())

            if not check:
                message = "You either tried to book for an expired deal or booked a date before today, please go back an try again. "
                return message
            result = reservations_sys.add_meeting(d_id, match_id, date_time_obj.date(), start_time, end_time)
            # return jsonify(result)
            return render_template('res_done.html')

        # return render_template('reservations.html')


def get_current_user():
    return current_user


if __name__ == '__main__':
    socketio.run(app, debug=True)
