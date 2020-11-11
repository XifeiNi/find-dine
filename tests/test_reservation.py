import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from server.app import app
from server.models import User_Profile, Right_Swipe, Match, Conversation, db
from flask import Flask, render_template, session

import unittest
from Classes.recommendation_system import Right_Swipes
from flask import session, Flask
import datetime
from datetime import date, datetime

class TestReservations(unittest.TestCase):

    def test_reservations(self):

        with app.app_context():

