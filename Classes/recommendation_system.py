import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from flask_login import current_user
from .google_maps import Google_Maps
from find_dine.server.models import User_Profile
# from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt
GOOGLE_MAPS_API_KEY = "AIzaSyDNSQlkoM44anY1fYWt-c84gFf_2S40lbg"

class Recommendation_System:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def getRecommendations(self, user_location):
        #current_user_id = current_user.id
        current_user_id = 1
        user = User_Profile()
        all_users = User_Profile.query.all()
        cur_user = User_Profile.query.filter_by(id=current_user_id).first()
        cur_user_sexuality = cur_user.gender_preference.name
        cur_user_min_age = cur_user.min_match_age
        cur_user_max_age = cur_user.max_match_age
        distances = []
        for user in all_users:
            user_age = self.calculateAge(user.dob)
            if user.username == cur_user.username:
                continue
            elif user.gender.name != cur_user_sexuality:
                print (user.gender)
                continue
            elif user.gender_preference.name != cur_user.gender.name:
                continue
            elif user_age < cur_user_min_age:
                continue
            elif user_age > cur_user_max_age:
                continue
            distance = self.Google_Maps_Api.get_distance(user_location, user.location, 'driving')
            if distance <= cur_user.max_match_distance:
                distance_append = {"match_user_username": user.username,
                                   "distance": distance}
                distances.append(distance_append)
        sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        return sorted_distances

    def calculateAge(self, born):
        today = date.today()
        try:
            birthday = born.replace(year=today.year)
            # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = born.replace(year=today.year,
                                    month=born.month + 1, day=1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year




