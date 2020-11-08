from flask_login import current_user
from .google_maps import Google_Maps
from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt
GOOGLE_MAPS_API_KEY = "AIzaSyDNSQlkoM44anY1fYWt-c84gFf_2S40lbg"

class Recommendation_System:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def getRecommendations(self, user_location):
        current_username = session['current_username']
        all_users = User_Profile.query.all()
        cur_user = User_Profile.query.filter_by(username=current_username).first()
        cur_user_sexuality = cur_user.gender_preference
        cur_user_min_age = cur_user.min_match_age
        cur_user_max_age = cur_user.max_match_age
        distances = []
        for user in all_users:
            user_age = self.calculateAge(user.dob)
            if user.username == current_username or user.gender != cur_user_sexuality or user_age >= cur_user_min_age or user_age > cur_user_max_age:
                continue
            distance = self.Google_Maps_Api.get_distance(user_location, user.location, 'driving')
            if distance <= cur_user.max_match_distance:
                distance_append = {"match_user_username": user.username,
                                   "distance": distance}
                distances.append(distance_append)
        sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        return sorted_distances

    def calculateAge(born):
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




