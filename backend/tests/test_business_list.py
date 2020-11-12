import sys
import os

from backend.server.models import Business_Profile, db, Deals

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.app import app
#from server.models import User_Profile, Right_Swipe, Messages, db
from flask import Flask, render_template, session

import unittest
from backend.Classes.recommendation_system import Recommendation_System
from flask import session, Flask
import datetime
from datetime import date, datetime


class TestBusinessList(unittest.TestCase):

    def test_business_list(self):
        with app.app_context():

            import csv
            with open('Business_Profile.csv', newline='') as csvfile:
                businesses_list = csv.reader(csvfile, delimiter='\n', quotechar='|')
                #result = []
                for row in businesses_list:
                    item: List[str] = row[0].split(',')

                    instance = db.session.query(Business_Profile).filter_by(id=int(item[0])).first()
                    if not instance:
                        business = Business_Profile(id=int(item[0]),
                                                    name=item[1],
                                                    email=item[2],
                                                    description=item[3],
                                                    address=item[4],
                                                    price_guide=item[5],
                                                    category=item[6])
                        db.session.add(business)
                        db.session.commit()

    def test_deals_list(self):

        with app.app_context():

            import csv
            with open('Deal.csv', newline='') as csvfile:
                deals_list = csv.reader(csvfile, delimiter='\n', quotechar='|')
                result = []
                for row in deals_list:
                    item: List[str] = row[0].split(',')

                    instance = db.session.query(Deals).filter_by(id=int(item[0])).first()
                    if not instance:
                        date_c = datetime.strptime(item[5], '%Y-%m-%d')
                        date_e = datetime.strptime(item[6], '%Y-%m-%d')
                        deals = Deals(id=int(item[0]),
                                      business_id=int(item[1]),
                                      deal_name=item[2],
                                      description=item[3],
                                      discount_percentage=int(item[4]),
                                      date_created=date_c,
                                      date_expiry=date_e)
                        db.session.add(deals)
                        db.session.commit()