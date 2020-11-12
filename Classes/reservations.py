import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from find_dine.server.models import Business_Profile, Deals, Meeting, Match, db, User_Profile


from flask_login import current_user
from .google_maps import Google_Maps
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt
from sqlalchemy import or_

class Reservation_system:

    def get_matched_users(self,user_id):
        all_matches = Match.query.filter(or_(Match.first_swiper == user_id, Match.second_swiper == user_id)).all()
        # print(all_matches)
        matched_users = []

        for match in all_matches:

            if match.first_swiper == user_id:
                user = User_Profile.query.filter_by(id=match.second_swiper).first()
                name = user.f_name + " " + user.l_name
                matched_users.append({
                    "user_id": user.id,
                    "match_id": match.id,
                    "user_name": name
                })

            if match.second_swiper == user_id:
                user = User_Profile.query.filter_by(id=match.first_swiper).first()
                name = user.f_name + " " + user.l_name
                matched_users.append({
                    "id": user.id,
                    "match_id": match.id,
                    "user_name": name
                })

        return matched_users

    def generate_meeting_id(self):
        num = (Meeting.query.order_by(Meeting.id.desc()).first())
        if num is None:
            return 1
        else:
            new_id = num.id + 1
            return new_id

    def add_meeting(self, deal_id, match_id, date_of_meeting, start_t, end_t):
        meeting_id = self.generate_meeting_id()
        result = []
        meeting = Meeting(
            id=meeting_id,
            deals_id=deal_id,
            date_meeting=date_of_meeting,
            match_id=match_id,
            time_start=str(start_t),
            time_end=str(end_t)
        )
        db.session.add(meeting)
        db.session.commit()

        result.append({
            "id": meeting_id,
            "deals_id": deal_id,
            "match_id": match_id,
            "date_meeting": date_of_meeting,
            "time_start": start_t,
            "time_end": end_t,
        })

        return result

    def check_date(self, d_id, date_of_meeting):

        deal = Deals.query.filter_by(id=d_id).first()

        if deal.date_expiry > date_of_meeting:
            if date_of_meeting > datetime.date.today():
                return True

        return False