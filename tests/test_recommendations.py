import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from find_dine.server.app import app
from find_dine.server.models import User_Profile, db
from flask import Flask, render_template, session

import unittest
from Classes.recommendation_system import Recommendation_System
from flask import session, Flask
import datetime
from datetime import date


class TestRecommendationSystem(unittest.TestCase):

    def test_recommend_food(self):
        rec_sys = Recommendation_System()


        origin = "Main Library, University of New South Wales, Sydney, Australia"
        loc2 = "Colombo House, University of New South Wales, Sydney, Australia"
        loc3 = "Keith Burrows Theatre, Univeristy of New South Wales, Sydney, Australia"
        loc4="New York, NY, USA"
        with app.app_context():
        # radius = 500
        # day_of_week = 2
        # start_time = datetime.time(hour=13, minute=30) # start : 1:30pm
        # end_time = datetime.time(17, 0, 0) # next class: 5:00pm
        # owner_id = 1

        # events = Rec_Sys.recommend_food(owner, origin, radius, day_of_week, start_time, end_time)
        #     test1 = User_Profile(f_name="Test",
        #                          l_name="one",
        #                          email_address="test1@gmail.com",
        #                          username="Test1",
        #                          password_hash="Test1",
        #                          gender="male",
        #                          gender_preference="male",
        #                          max_match_distance=25,
        #                          min_match_age=15,
        #                          max_match_age=25,
        #                          bio="I am horny",
        #                          location="aaaa",
        #                          dob=date(2000,1, 1))
        #
        #     test2=User_Profile(f_name="Test",
        #                          l_name="two",
        #                          email_address="test2@gmail.com",
        #                          username="Test2",
        #                          password_hash="Test2",
        #                          gender="male",
        #                          gender_preference="male",
        #                          max_match_distance=25,
        #                          min_match_age=15,
        #                          max_match_age=25,
        #                          bio="I am horny",
        #                          location=loc2,
        #                        dob=date(2000,6,10))
        #     test3 = User_Profile(f_name="Test",
        #                          l_name="three",
        #                          email_address="test3@gmail.com",
        #                          username="Test3",
        #                          password_hash="Test3",
        #                          gender="female",
        #                          gender_preference="male",
        #                          max_match_distance=25,
        #                          min_match_age=15,
        #                          max_match_age=25,
        #                          bio="I am horny",
        #                          location=loc3,
        #                        dob=date(2005,4,13))
        #     test4= User_Profile(f_name="Test",
        #                          l_name="four",
        #                          email_address="test4@gmail.com",
        #                          username="Test4",
        #                          password_hash="Test4",
        #                          gender="male",
        #                          gender_preference="female",
        #                          max_match_distance=25,
        #                          min_match_age=15,
        #                          max_match_age=25,
        #                          bio="I am horny",
        #                          location=loc4,
        #                        dob=date(2003,12,1))
        #     db.session.add(test1)
        #     db.session.add(test2)
        #     db.session.add(test3)
        #     db.session.add(test4)
        #     db.session.commit()
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

        #assert False