import sys
import os


sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.app import app
from backend.server.models import User_Profile, Right_Swipe, db
from flask import Flask, render_template, session

import unittest
from backend.Classes.recommendation_system import Recommendation_System
from flask import session, Flask
import datetime
from datetime import date, datetime


class TestRecommendationSystem(unittest.TestCase):

    def test_recommend_matches(self, origin):
        rec_sys = Recommendation_System()



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

        #assert False