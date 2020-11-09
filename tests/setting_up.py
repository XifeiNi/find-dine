import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from find_dine.server.app import app
from find_dine.server.models import User_Profile, Right_Swipe, db
from flask import Flask, render_template, session

import unittest
from Classes.recommendation_system import Recommendation_System
from flask import session, Flask
import datetime
from datetime import date, datetime


class TestSettingUp(unittest.TestCase):

    def test_setting_up(self):



        origin = "Main Library, University of New South Wales, Sydney, Australia"
        loc2 = "Colombo House, University of New South Wales, Sydney, Australia"
        loc3 = "Keith Burrows Theatre, Univeristy of New South Wales, Sydney, Australia"
        loc4="Library building Level 11, Library Walk, Kensington NSW 2052"
        loc5 = "Law Building, Union Rd, Kensington NSW 2035"
        loc6 = "7 Water St, Lidcombe NSW 2141"
        loc7 = "12 Smallwood Ave, Homebush NSW 2140"
        with app.app_context():
        # radius = 500
        # day_of_week = 2
        # start_time = datetime.time(hour=13, minute=30) # start : 1:30pm
        # end_time = datetime.time(17, 0, 0) # next class: 5:00pm
        # owner_id = 1

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
            db.session.add(swipe1)
            db.session.add(swipe2)
            db.session.commit()