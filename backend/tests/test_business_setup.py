import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.business.app import app
from backend.server.models import Business_Profile, Deals, db
from flask import Flask, render_template, session

import unittest
from backend.Classes.recommendation_system import Recommendation_System
from flask import session, Flask
import datetime
from datetime import date, datetime


class TestSettingUp(unittest.TestCase):

    def test_setting_up(self):
        with app.app_context():
            test1 = Business_Profile(name="Test1 Corporation",
                                     email="test1@corporation.com",
                                     password="test1@corporation.com",
                                     description="Test1 Corporation",
                                     address="1 Test1 Street, Sydney NSW 2000",
                                     price_guide="low",
                                     phone_number="0411111111",
                                     category="casual")
            db.session.add(test1)
            db.session.commit()
            deal1=Deals(business_id=1,
                       deal_name="Deal1",
                       description="Deal1 with Business " + str(1),
                       discount_percentage=10,
                       date_expiry=date(2021, 1, 1),
                       date_created=date.today())
            deal2 = Deals(business_id=1,
                         deal_name="Deal2",
                         description="Deal2 with Business " + str(1),
                         discount_percentage=30,
                         date_expiry=date(2022, 3, 5),
                         date_created=date(2020, 11, 2))
            deal3=Deals(business_id=1,
                       deal_name="Deal3",
                       description="Deal3 with Business " + str(1),
                       discount_percentage=34,
                       date_expiry=date(2020, 11, 11),
                       date_created=date.today())
            db.session.add(deal1)
            db.session.add(deal2)
            db.session.add(deal3)
            db.session.commit()
    #
    # def test_setting_up_conversations(self):
    #
    #     with app.app_context():
    #         message1= Messages(room="6+3",
    #                            sender_username=3,
    #                            time_sent=datetime.now(),
    #                            message="This is the first message at " + str(datetime.now()))
    #         db.session.add(message1)
    #         db.session.commit()
    #         message2= Messages(room="6+3",
    #                            sender_username=6,
    #                            time_sent=datetime.now(),
    #                            message="This is the second message at " + str(datetime.now()))
    #         db.session.add(message2)
    #         db.session.commit()


