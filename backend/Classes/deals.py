import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.models import Business_Profile, Deals


from flask_login import current_user
from .google_maps import Google_Maps
from backend.server.models import User_Profile, Conversation, Messages, Match, db
# from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt


class Deals_system:

    def all_businesses_list(self):

        business_list = Business_Profile.query.all()
        result = []
        for record in business_list:
            result.append({
                "id": int(record.id),
                "name": record.name,
                "email": record.email,
                "description": record.description,
                "address": record.address,
                "price_guide": record.price_guide,
                "category": record.category
            })

        return result

    def all_deals_list(self):
        deals_list = Deals.query.all()
        result = []
        for record in deals_list:
            result.append({
                "id": int(record.id),
                "business_id": record.business_id,
                "deal_name": record.deal_name,
                "description": record.description,
                "discount_percentage": record.discount_percentage,
                "date_created": record.date_created,
                "date_expiry": record.date_expiry
                # "date_created": datetime.date.strptime(item[6], "%d %b %Y")
            })

        return result

