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
            user_id = 6
            right_swipe_1 = Right_Swipe(time=datetime.now(),
                                        swiper_id=user_id,
                                        target_id=1,
                                        became_match=False)

            right_swipe_2 = Right_Swipe(time=datetime.now(),
                                        swiper_id=1,
                                        target_id=user_id,
                                        became_match=True)

            db.session.add(right_swipe_1)
            db.session.add(right_swipe_2)
            db.session.commit()

            room_id = str(right_swipe_1.swiper_id) + "+" + str(right_swipe_1.target_id)

            conversation = Conversation(room=room_id,
                                        username_one=right_swipe_1.swiper_id,
                                        username_two=right_swipe_1.target_id)
            db.session.add(conversation)
            db.session.commit()

            match = Match(distance=12,
                          created=datetime.now(),
                          first_swiper=right_swipe_1.target_id,
                          second_swiper=right_swipe_1.swiper_id,
                          conversation_id=room_id)
            db.session.add(match)
            db.session.commit()

