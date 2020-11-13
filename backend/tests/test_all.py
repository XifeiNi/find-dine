import sys
import os
import unittest
from datetime import date, datetime

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.Classes.recommendation_system import Recommendation_System, Right_Swipes
from backend.Classes.message_system import Message_System
from backend.server.models import User_Profile, db, Right_Swipe, Messages, Conversation, Match

from backend.server.simulation import app, signup, login, current_user, logout, view_blocked, view_blockable, block, \
    view_profile, update_gender_preference, update_min_match_age, update_max_match_age, update_max_match_distance, \
    update_bio

from backend.server.simulation import app, signup, login, current_user, logout
from backend.Classes.google_maps import Google_Maps


GOOGLE_MAPS_API_KEY = "AIzaSyCqVpb4IWMDpYg2mGo-zv6l6XKIp_sESwo"


class TestProgram():

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def command_centre(self):
        with app.app_context():
            print("Testing authentication:")
            command = ""
            while True:
                command = input(

                    "commands: signup, signup dummy, login, logout, view blocked, block, profile, recommendations,"
                    "swipe_right, my_conversations, view conversation, send_message, exit: ")

                if command == "exit":
                    break

                if command == "get user":
                    print(current_user.get_cu())
                    continue

                if command == "signup":
                    request = {'email': input("enter email: "), 'username': input("enter username: "),
                               'f_name': input("enter first name: "), 'l_name': input("enter last name: "),
                               'password': input("enter password: "), 'password_repeat': input("confirm password: "),
                               'dob': input("enter DOB (YYYY-MM-DD): "),
                               'min_target': input("enter min matching age: "),
                               'max_target': input("enter max matching age: "),
                               'gender': input("enter gender (male, female, other): "),
                               'gender_preference': input("enter gender preference (male, female, everyone): "),
                               'bio': input("enter bio: "), 'location': input("enter matching location: "),
                               'max_match_distance': input("enter max match distance: ")}

                    signup(request)
                    continue

                if command == "signup dummy":
                    request = {'email': 'sascha.graham@gmail.com', 'username': 'sascha', 'f_name': 'sascha',
                               'l_name': 'graham', 'password': 'awd', 'password_repeat': 'awd', 'dob': '1999-11-02',
                               'min_target': '16', 'max_target': '22', 'gender': 'male',
                               'gender_preference': 'everyone',
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

                if command == "view blocked":
                    print("blocked users: ")
                    print(view_blocked())
                    continue

                if command == "block":
                    print("blockable users: ")
                    print(view_blockable())
                    target_user = input("select user, \\n to abort: ")
                    if target_user == "":
                        continue
                    block(target_user)

                if command == "profile":
                    print("profile:\n\n")
                    print(view_profile())
                    profile_command = input("commands: edit match preferences (1), edit bio(2), exit profile (3): ")
                    if profile_command == "1":
                        edit = input(
                            "gender preference (1), min match age (2), max match age (3), max match distance (4): ")
                        if edit == "1":
                            pref = input("new gender preference (male, female, everyone): ")
                            update_gender_preference(pref)
                        if edit == "2":
                            age = input("new min match age: ")
                            update_min_match_age(age)
                        if edit == "3":
                            age = input("new max match age: ")
                            update_max_match_age(age)
                        if edit == "4":
                            dist = input("new max match distance: ")
                            update_max_match_distance(dist)
                    if profile_command == "2":
                        bio = input("new bio (150 chars): ")
                        update_bio(bio)
                    if profile_command == "3":
                        pass

                if command == "recommendations":
                    self.recommendations()
                if command == "swipe_right":
                    self.right_swipe()
                if command == "my_conversations":
                    self.get_conversations()
                if command == "view conversation":
                    self.get_conversation_messages()
                if command == "send_message":
                    self.send_message()


    def recommendations(self):
        # origin = "Main Library, University of New South Wales, Sydney, Australia"
        curr_user = current_user.get_cu()
        if curr_user is None:
            print ("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id
        user = User_Profile.query.filter_by(id=current_user_id).first()
        origin = input("Your current locaton please: ")


        recs_sys = Recommendation_System()
        # current_user_id = current_user.id
        # current_user_id = current_user.id
        curr_user = current_user.get_cu()
        if curr_user is None:
            print ("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id
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


    def right_swipe(self):
        curr_user = current_user.get_cu()
        if curr_user is None:
            print ("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id
        user = User_Profile.query.filter_by(id=current_user_id).first()
        username = input("Username of person, you want to swipe on: ")
        target_user = User_Profile.query.filter_by(username=username).first()
        if target_user is None:
            print ("We couldn't find an user with that username, please check the username and try again")
            return
        distance = self.Google_Maps_Api.get_distance(user.location, target_user.location, 'driving')
        if distance == -1:
            print("Google Maps could not return a possible distance. Check the error message from Google")
            return
        match_dict = {"match_user_username": username,
                      "distance": distance}


        right_swipes = Right_Swipes()
        current_user_id = curr_user.id
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

    def get_conversations(self):
        curr_user = current_user.get_cu()
        if curr_user is None:
            print("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id

        message_sys = Message_System()
        conversations = message_sys.getConversations(current_user_id)
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

    def get_conversation_messages(self):
        curr_user = current_user.get_cu()
        if curr_user is None:
            print("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id
        target_username = input("Which conversation would you like to view: ")
        target_user = User_Profile.query.filter_by(username=target_username).first()
        if target_user is None:
            print ("We couldn't find a user with that username, please check the username and try again")
            return
        username_one = User_Profile.query.filter_by(id=current_user_id).first().id
        username_two = target_user.id
        if (Conversation.query.filter_by(username_one=username_one).filter_by(username_two=username_two).first()) is not None:
            room_id=Conversation.query.filter_by(username_one=username_one).filter_by(username_two=username_two).first().room
        elif (Conversation.query.filter_by(username_two=username_one).filter_by(username_one=username_two).first()) is not None:
            room_id=Conversation.query.filter_by(username_two=username_one).filter_by(username_one=username_two).first().room
        else:
            print("Conversation with " + target_username + " does not exist in our system. Are you sure, its the right username?")
            return


        message_sys = Message_System()
        conversation, messages = message_sys.getMessages(room_id, current_user_id)
        print("########################")
        print("Username: ", conversation['conversation_username'])
        print("***********************")
        for message in messages:
            print("Message Sender: ", message['message_username'])
            print("Message: ", message['message'])
            print("Time: ", message['time_sent'])

    def send_message(self):
        curr_user = current_user.get_cu()
        if curr_user is None:
            print("Something is wrong. Someone must be logged in, please login first")
            return
        current_user_id = curr_user.id
        while True:
            try:
                username_input = input("Who would you like to message?: ")
            except KeyboardInterrupt:
                print() # newline
                break
            while True:
                try:
                    message_input = input("Message: ")
                except KeyboardInterrupt:
                    print() # newline
                    break
                json = {'user_name': username_input,
                        'message': message_input}


                username = User_Profile.query.filter_by(username=json['user_name']).first()
                if username is None:
                    # socketio.emit('my response', json, callback="Something is wrong, Username cannot be found")
                    # exit(100)
                    print("We couldn't find a user with that username, please check the username and try again")
                    return

                conversation = Conversation.query.filter_by(username_one=username.id).filter_by(
                    username_two=current_user_id).first()
                if conversation is None:
                    conversation = Conversation.query.filter_by(username_two=username.id).filter_by(
                        username_one=current_user_id).first()
                if conversation is None:
                    # socketio.emit('my response', json, callback="Something is wrong, Conversation Room cannot be found")
                    # exit(200)
                    print("Conversation with " + username_input + " does not exist in our system. Are you sure, its the right username?")
                    return
                room = conversation.room
                message = Messages(room=room,
                                   sender_username=current_user_id,
                                   time_sent=datetime.now(),
                                   message=json['message'])
                db.session.add(message)
                db.session.commit()
                message_sys = Message_System()
                conversation, messages = message_sys.getMessages(room, current_user_id)
                print("########################")
                print("Username: ", conversation['conversation_username'])
                print("***********************")
                for message in messages:
                    print("Message Sender: ", message['message_username'])
                    print("Message: ", message['message'])
                    print("Time: ", message['time_sent'])
    #
# class TestAll(unittest.TestCase):
#
#     def test_all(self):
#         origin = "Main Library, University of New South Wales, Sydney, Australia"
#         loc2 = "Colombo House, University of New South Wales, Sydney, Australia"
#         loc3 = "Keith Burrows Theatre, Univeristy of New South Wales, Sydney, Australia"
#         loc4 = "Library building Level 11, Library Walk, Kensington NSW 2052"
#         loc5 = "Law Building, Union Rd, Kensington NSW 2035"
#         loc6 = "7 Water St, Lidcombe NSW 2141"
#         loc7 = "12 Smallwood Ave, Homebush NSW 2140"
#         with app.app_context():
#             # radius = 500
#             # day_of_week = 2
#             # start_time = datetime.time(hour=13, minute=30) # start : 1:30pm
#             # end_time = datetime.time(17, 0, 0) # next class: 5:00pm
#             # owner_id = 1
#
#             # events = Rec_Sys.recommend_food(owner, origin, radius, day_of_week, start_time, end_time)
#             test1 = User_Profile(f_name="Test",
#                                  l_name="one",
#                                  email_address="test1@gmail.com",
#                                  username="Test1",
#                                  password_hash="Test1",
#                                  gender="male",
#                                  gender_preference="male",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location="aaaa",
#                                  dob=date(2000, 1, 1))
#
#             test2 = User_Profile(f_name="Test",
#                                  l_name="two",
#                                  email_address="test2@gmail.com",
#                                  username="Test2",
#                                  password_hash="Test2",
#                                  gender="male",
#                                  gender_preference="male",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc2,
#                                  dob=date(2000, 6, 10))
#             test3 = User_Profile(f_name="Test",
#                                  l_name="three",
#                                  email_address="test3@gmail.com",
#                                  username="Test3",
#                                  password_hash="Test3",
#                                  gender="female",
#                                  gender_preference="male",
#                                  max_match_distance=30,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc3,
#                                  dob=date(2005, 4, 13))
#             test4 = User_Profile(f_name="Test",
#                                  l_name="four",
#                                  email_address="test4@gmail.com",
#                                  username="Test4",
#                                  password_hash="Test4",
#                                  gender="male",
#                                  gender_preference="female",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc4,
#                                  dob=date(2003, 12, 1))
#             test5 = User_Profile(f_name="Test",
#                                  l_name="five",
#                                  email_address="test5@gmail.com",
#                                  username="Test5",
#                                  password_hash="Test5",
#                                  gender="male",
#                                  gender_preference="female",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc5,
#                                  dob=date(1998, 10, 10))
#             test6 = User_Profile(f_name="Test",
#                                  l_name="siz",
#                                  email_address="test6@gmail.com",
#                                  username="Test6",
#                                  password_hash="Test6",
#                                  gender="male",
#                                  gender_preference="female",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc6,
#                                  dob=date(2001, 6, 12))
#             test7 = User_Profile(f_name="Test",
#                                  l_name="seven",
#                                  email_address="test7@gmail.com",
#                                  username="Test7",
#                                  password_hash="Test7",
#                                  gender="male",
#                                  gender_preference="female",
#                                  max_match_distance=25,
#                                  min_match_age=15,
#                                  max_match_age=25,
#                                  bio="I am horny",
#                                  location=loc7,
#                                  dob=date(1998, 5, 4))
#             db.session.add(test1)
#             db.session.add(test2)
#             db.session.add(test3)
#             db.session.add(test4)
#             db.session.add(test5)
#             db.session.add(test6)
#             db.session.add(test7)
#             db.session.commit()
#
#             swipe1 = Right_Swipe(time=datetime.now(),
#                                  swiper_id=4,
#                                  target_id=3)
#             swipe2 = Right_Swipe(time=datetime.now(),
#                                  swiper_id=5,
#                                  target_id=3)
#             swipe3 = Right_Swipe(time=datetime.now(),
#                                  swiper_id=6,
#                                  target_id=3)
#             db.session.add(swipe1)
#             db.session.add(swipe2)
#             db.session.add(swipe3)
#             db.session.commit()
#
#     def test_all_conversations(self):
#         with app.app_context():
#             message1 = Messages(room="6+3",
#                                 sender_username=3,
#                                 time_sent=datetime.now(),
#                                 message="This is the first message at " + str(datetime.now()))
#             db.session.add(message1)
#             db.session.commit()
#             message2 = Messages(room="6+3",
#                                 sender_username=6,
#                                 time_sent=datetime.now(),
#                                 message="This is the second message at " + str(datetime.now()))
#             db.session.add(message2)
#             db.session.commit()
#
# class TestRecommendationSystem(unittest.TestCase):
#
#     def test_recommend_matches(self):
#         # simulate a login of a user
#
#         rec_sys = Recommendation_System()
#
#
#
#         origin = "Main Library, University of New South Wales, Sydney, Australia"
#         loc2 = "Colombo House, University of New South Wales, Sydney, Australia"
#         loc3 = "Keith Burrows Theatre, Univeristy of New South Wales, Sydney, Australia"
#         loc4="Library building Level 11, Library Walk, Kensington NSW 2052"
#         loc5 = "Law Building, Union Rd, Kensington NSW 2035"
#         loc6 = "7 Water St, Lidcombe NSW 2141"
#         loc7 = "12 Smallwood Ave, Homebush NSW 2140"
#         with app.app_context():
#             login({'username': 'sascha', 'password': 'awd'})
#
#             recommendations = rec_sys.getRecommendations(origin, current_user.get_cu().id)
#
#             # self.assertTrue(len(recommendations) >= 1)
#             print(len(recommendations))
#             # To print during pytest, uncomment False Assertion
#             for recommendation in recommendations:
#                 # event.user_id = owner.id
#                 print("########################")
#                 # print("First Name: ", recommendation.f_name)
#                 # print ("Last Name: ", recommendation.l_name)
#                 # print("addr: ", event.addr)
#                 # print("start: ", event.start_time)
#                 # print("end: ", event.end_time)
#                 print("Username: ", recommendation['match_user_username'])
#                 print("Distance: ", recommendation['distance'])
#
#
# class TestRightSwipes(unittest.TestCase):
#
#     def test_right_swipes(self):
#
#         with app.app_context():
#
#             match_dict1 = {"match_user_username": "Test6",
#                            "distance": 26}
#             code = self.right_swipe_function(match_dict1)
#             print ("*********************************")
#             print (match_dict1)
#             print ("#################################")
#             print (code)
#
#             match_dict2={"match_user_username": "Test7",
#                            "distance": 22}
#             code = self.right_swipe_function(match_dict2)
#             print ("*********************************")
#             print (match_dict2)
#             print ("#################################")
#             print (code)
#
#             match_dict3 = {"match_user_username": "Test5",
#                            "distance": 1}
#             code = self.right_swipe_function(match_dict3)
#             print("*********************************")
#             print(match_dict3)
#             print("#################################")
#             print(code)
#
#
#     def right_swipe_function(self, match_dict):
#         right_swipes = Right_Swipes()
#         current_user_id = 3
#         target_id = User_Profile.query.filter_by(username=match_dict['match_user_username']).first().id
#         previous_swipe = right_swipes.right_swipes(match_dict, current_user_id, target_id)
#         if previous_swipe == 1:
#             second_right_swipe = Right_Swipe(time=datetime.now(),
#                                              swiper_id=current_user_id,
#                                              target_id=target_id,
#                                              became_match=True)
#             db.session.add(second_right_swipe)
#             db.session.commit()
#             room_id = str(target_id) + "+" + str(current_user_id)
#             conversation = Conversation(room=room_id,
#                                         username_one=target_id,
#                                         username_two=current_user_id)
#             db.session.add(conversation)
#             db.session.commit()
#             match = Match(distance=match_dict['distance'],
#                           created=datetime.now(),
#                           first_swiper=target_id,
#                           second_swiper=current_user_id,
#                           conversation_id=room_id)
#             db.session.add(match)
#             db.session.commit()
#             found_match = {"succesful_error_message": "Found a match",
#                            "successful_error_code": 0}
#             code = found_match
#             # socketio.emit("join_response", found_match)
#         elif previous_swipe == -1:
#             first_right_swipe = Right_Swipe(time=datetime.now(),
#                                             swiper_id=current_user_id,
#                                             target_id=target_id)
#             db.session.add(first_right_swipe)
#             db.session.commit()
#             first_right_swipe = {"successful_error_message": "Request has been included into our system",
#                                  "successful_error_code": 1}
#             code = first_right_swipe
#             # socketio.emit("join_response", first_right_swipe)
#         else:
#             error_code = {"successful_error_message": "Something went wrong",
#                           "successful_error_code": -1}
#             code = error_code
#         return code
#             # socketio.emit("join_response", error_code)
#
# class TestMessageSystem(unittest.TestCase):
#
#     def test_message_system(self):
#         message_sys = Message_System()
#         with app.app_context():
#             login({'username': 'Test1', 'password': 'Test1'})
#             conversations = message_sys.getConversations(current_user.get_cu().id)
#             for conversation in conversations:
#                 print("########################")
#                 # print("First Name: ", recommendation.f_name)
#                 # print ("Last Name: ", recommendation.l_name)
#                 # print("addr: ", event.addr)
#                 # print("start: ", event.start_time)
#                 # print("end: ", event.end_time)
#                 print("Username: ", conversation['username'])
#                 print("Last_Message: ", conversation['last_message'])
#                 print ("Time: ", conversation['time'])
#
#     def test_conversation_system(self):
#
#         room_id = "6+3"
#         message_sys = Message_System()
#         with app.app_context():
#             login({'username': 'Test3', 'password': 'Test3'})
#
#             conversation, messages = message_sys.getMessages(room_id, current_user.get_cu().id)
#             print("########################")
#             print("Username: ", conversation['conversation_username'])
#             print ("***********************")
#             for message in messages:
#                 print("########################")
#                 # print("First Name: ", recommendation.f_name)
#                 # print ("Last Name: ", recommendation.l_name)
#                 # print("addr: ", event.addr)
#                 # print("start: ", event.start_time)
#                 # print("end: ", event.end_time)
#                 print("Message Sender: ", message['message_username'])
#                 print("Message: ", message['message'])
#                 print ("Time: ", message['time_sent'])
#
#         #assert False
#

if __name__ == '__main__':
    test_program = TestProgram()
    test_program.command_centre()
