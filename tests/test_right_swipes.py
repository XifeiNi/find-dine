import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from find_dine.server.app import app
from find_dine.server.models import User_Profile, Right_Swipe, Match, Conversation, db
from flask import Flask, render_template, session

import unittest
from Classes.recommendation_system import Right_Swipes
from flask import session, Flask
import datetime
from datetime import date, datetime

class TestRightSwipes(unittest.TestCase):

    def test_right_swipes(self):

        with app.app_context():

            match_dict1 = {"match_user_username": "Test6",
                           "distance": 26}
            code = self.right_swipe_function(match_dict1)
            print ("*********************************")
            print (match_dict1)
            print ("#################################")
            print (code)

            match_dict2={"match_user_username": "Test7",
                           "distance": 22}
            code = self.right_swipe_function(match_dict2)
            print ("*********************************")
            print (match_dict2)
            print ("#################################")
            print (code)

            match_dict3 = {"match_user_username": "Test5",
                           "distance": 1}
            code = self.right_swipe_function(match_dict3)
            print("*********************************")
            print(match_dict3)
            print("#################################")
            print(code)


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
            # socketio.emit("join_response", error_code)


