import sys
import os
import unittest
from datetime import date, datetime

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.models import User_Profile, db, Right_Swipe, Messages, Conversation, Match
from backend.server.simulation import app, signup, login, current_user, logout
from backend.tests.test_recommendations import TestRecommendationSystem
from backend.Classes.recommendation_system import Recommendation_System, Right_Swipes

# app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'user_side#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test_script.db'
db.init_app(app)
# socketio = SocketIO(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

# needed for login manager implementation. Gets user object from id

with app.app_context():
    db.create_all()


class TestAll(unittest.TestCase):
    def test_all(self):
        with app.app_context():
            self.set_up()
            print("Testing authentication:")
            command = ""
            while True:
                command = input("commands: signup, login, logout, exit, recommendations: ")
                if command == "exit":
                    break

                if command == "get user":
                    print(current_user.cu)
                    continue

                if command == "signup":
                    request = {'email': input("enter email: "), 'username': input("enter username: "),
                               'f_name': input("enter first name: "), 'l_name': input("enter last name: "),
                               'password': input("enter password: "), 'password_repeat': input("confirm password: "),
                               'dob': input("enter DOB (YYYY-MM-DD): "), 'min_target': input("enter min matching age: "),
                               'max_target': input("enter max matching age: "),
                               'gender': input("enter gender (male, female, other): "),
                               'gender_preference': input("enter gender preference (male, female, everyone): "),
                               'bio': input("enter bio: "), 'location': input("enter matching location: "),
                               'max_match_distance': input("enter max match distance: ")}

                    request = {'email': 'sascha.graham@gmail.com', 'username': 'sascha', 'f_name': 'sascha',
                               'l_name': 'graham', 'password': 'awd', 'password_repeat': 'awd', 'dob': '1999-11-02',
                               'min_target': '16', 'max_target': '22', 'gender': 'male', 'gender_preference': 'everyone',
                               'bio': 'awd', 'location': '23 Cameron Ave Artarmon', 'max_match_distance': '200'}

                    signup(request)
                    continue

                if command == "login":
                    request = {'username': input("enter username: "), 'password': input("enter password: ")}

                    login(request)
                    continue

                if command == "logout":
                    logout()
                    continue
                if command == "recommendations":
                    self.recommendations()

# class TestAll(unittest.TestCase):

    def set_up(self):
        loc2 = "Colombo House, University of New South Wales, Sydney, Australia"
        loc3 = "Keith Burrows Theatre, Univeristy of New South Wales, Sydney, Australia"
        loc4="Library building Level 11, Library Walk, Kensington NSW 2052"
        loc5 = "Law Building, Union Rd, Kensington NSW 2035"
        loc6 = "7 Water St, Lidcombe NSW 2141"
        loc7 = "12 Smallwood Ave, Homebush NSW 2140"
        with app.app_context():
        # events = Rec_Sys.recommend_food(owner, origin, radius, day_of_week, start_time, end_time)
            test1 = User_Profile(f_name="Test",
                                 l_name="one",
                                 email_address="test1@gmail.com",
                                 username="Test1",
                                 password_hash="Test1",
                                 gender="male",
                                 gender_preference="male",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location="aaaa",
                                 dob=date(2000, 1, 1))

            test2 = User_Profile(f_name="Test",
                                 l_name="two",
                                 email_address="test2@gmail.com",
                                 username="Test2",
                                 password_hash="Test2",
                                 gender="male",
                                 gender_preference="male",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc2,
                                 dob=date(2000, 6, 10))
            test3 = User_Profile(f_name="Test",
                                 l_name="three",
                                 email_address="test3@gmail.com",
                                 username="Test3",
                                 password_hash="Test3",
                                 gender="female",
                                 gender_preference="male",
                                 max_match_distance=30,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc3,
                                 dob=date(2005, 4, 13))
            test4 = User_Profile(f_name="Test",
                                 l_name="four",
                                 email_address="test4@gmail.com",
                                 username="Test4",
                                 password_hash="Test4",
                                 gender="male",
                                 gender_preference="female",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc4,
                                 dob=date(2003, 12, 1))
            test5 = User_Profile(f_name="Test",
                                 l_name="five",
                                 email_address="test5@gmail.com",
                                 username="Test5",
                                 password_hash="Test5",
                                 gender="male",
                                 gender_preference="female",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc5,
                                 dob=date(1998, 10, 10))
            test6 = User_Profile(f_name="Test",
                                 l_name="siz",
                                 email_address="test6@gmail.com",
                                 username="Test6",
                                 password_hash="Test6",
                                 gender="male",
                                 gender_preference="female",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc6,
                                 dob=date(2001, 6, 12))
            test7 = User_Profile(f_name="Test",
                                 l_name="seven",
                                 email_address="test7@gmail.com",
                                 username="Test7",
                                 password_hash="Test7",
                                 gender="male",
                                 gender_preference="female",
                                 max_match_distance=25,
                                 min_match_age=15,
                                 max_match_age=25,
                                 bio="I am horny",
                                 location=loc7,
                                 dob=date(1998, 5, 4))
            db.session.add(test1)
            db.session.add(test2)
            db.session.add(test3)
            db.session.add(test4)
            db.session.add(test5)
            db.session.add(test6)
            db.session.add(test7)
            db.session.commit()

            swipe1 = Right_Swipe(time=datetime.now(),
                                 swiper_id=4,
                                 target_id=3)
            swipe2 = Right_Swipe(time=datetime.now(),
                                 swiper_id=5,
                                 target_id=3)
            swipe3= Right_Swipe(time=datetime.now(),
                                swiper_id=6,
                                target_id=3)
            db.session.add(swipe1)
            db.session.add(swipe2)
            db.session.add(swipe3)
            db.session.commit()

    def recommendations(self):
        rec_sys = Recommendation_System()
        # origin = "Main Library, University of New South Wales, Sydney, Australia"
        origin = input("Your current location: ")

        with app.app_context():
            recommendations = rec_sys.getRecommendations(origin)

            # self.assertTrue(len(recommendations) >= 1)
            print(len(recommendations))
            # To print during pytest, uncomment False Assertion
            for recommendation in recommendations:
                # event.user_id = owner.id
                print("########################")
                # print("First Name: ", recommendation.f_name)
                # print ("Last Name: ", recommendation.l_name)
                # print("addr: ", event.addr)
                # print("start: ", event.start_time)
                # print("end: ", event.end_time)
                print("Username: ", recommendation['match_user_username'])
                print("Distance: ", recommendation['distance'])

    def right_swipes(self, user_location, target_username):
            # match_dict1 = {"match_user_username": "Test6",
            #                "distance": 26}
            # code = self.right_swipe_function(match_dict1)
            # print ("*********************************")
            # print (match_dict1)
            # print ("#################################")
            # print (code)
            #
            # match_dict2={"match_user_username": "Test7",
            #                "distance": 22}
            # code = self.right_swipe_function(match_dict2)
            # print ("*********************************")
            # print (match_dict2)
            # print ("#################################")
            # print (code)
            #
            # match_dict3 = {"match_user_username": "Test5",
            #                "distance": 1}
            # code = self.right_swipe_function(match_dict3)
            # print("*********************************")
            # print(match_dict3)
            # print("#################################")
            # print(code)

            distance = self.Google_Maps_Api.get_distance(user_location, user.location, 'driving')
            if distance == -1:
                print("Google Maps could not return a possible distance. Check the error message from Google")
                exit(300)
            if distance <= cur_user.max_match_distance:
                distance_append = {"match_user_username": user.username,
                                   "distance": distance}


    def right_swipe_function(self, match_dict):
        right_swipes = Right_Swipes()
        current_user_id = 3
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
            # socket

    def get_conversations(self):

            message1= Messages(room="6+3",
                               sender_username=3,
                               time_sent=datetime.now(),
                               message="This is the first message at " + str(datetime.now()))
            db.session.add(message1)
            db.session.commit()
            message2= Messages(room="6+3",
                               sender_username=6,
                               time_sent=datetime.now(),
                               message="This is the second message at " + str(datetime.now()))
            db.session.add(message2)
            db.session.commit()
