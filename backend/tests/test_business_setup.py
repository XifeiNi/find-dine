import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.business.app import app
from backend.server.models import Business_Profile, Deals, Meeting, db
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
            test2 = Business_Profile(name="Bang's",
                                     email="test2@corporation.com",
                                     password="test2@corporation.com",
                                     description="Lots of different meat options, dozens of pasta options and a mix of all of this in our fast-food dishes.",
                                     price_guide = "low",
                                     phone_number = "0411111111",
                                     category = "casual")
            test3 = Business_Profile(name="LeGusto",
                                     email="test3@corporation.com",
                                     password="test3@corporation.com",
                                     description="Surrounded by the best of the Italian cuisine, we can make you just fall in love with our pasta.",
                                     price_guide="low",
                                     phone_number="0411111111",
                                     category="fine")
            db.session.add(test1)
            db.session.add(test2)
            db.session.add(test3)
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
            deal4=Deals(business_id=2,
                          deal_name="Deal4",
                          description="Deal4 with Business " + str(1),
                          discount_percentage=35,
                          date_expiry=date(2021, 11, 11),
                          date_created=date.today())
            deal5=Deals(business_id=2,
                          deal_name="Deal5",
                          description="Deal5 with Business " + str(1),
                          discount_percentage=20,
                          date_expiry=date(2021, 11, 10),
                          date_created=date.today())
            db.session.add(deal1)
            db.session.add(deal2)
            db.session.add(deal3)
            db.session.add(deal4)
            db.session.add(deal5)
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


