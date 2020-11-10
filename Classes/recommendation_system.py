import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from flask_login import current_user
from .google_maps import Google_Maps
from find_dine.server.models import User_Profile, Right_Swipe, Match, Conversation, db
# from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt
# good API key
# GOOGLE_MAPS_API_KEY = "AIzaSyCqVpb4IWMDpYg2mGo-zv6l6XKIp_sESwo"
# shitty API key
GOOGLE_MAPS_API_KEY = "AIzaSyDNSQlkoM44anY1fYWt-c84gFf_2S40lbg"


class Recommendation_System:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def getRecommendations(self, user_location):
        #current_user_id = current_user.id
        current_user_id = 3
        # user = User_Profile()
        # all_users = User_Profile.query.all()
        # cur_user = User_Profile.query.filter_by(id=current_user_id).first()
        # cur_user_sexuality = cur_user.gender_preference.name
        # cur_user_min_age = cur_user.min_match_age
        # cur_user_max_age = cur_user.max_match_age
        # distances = []
        # for user in all_users:
        #     user_age = self.calculateAge(user.dob)
        #     if user.username == cur_user.username:
        #         continue
        #     elif user.gender.name != cur_user_sexuality:
        #         print (user.gender)
        #         continue
        #     elif user.gender_preference.name != cur_user.gender.name:
        #         continue
        #     elif user_age < cur_user_min_age:
        #         continue
        #     elif user_age > cur_user_max_age:
        #         continue
        #     distance = self.Google_Maps_Api.get_distance(user_location, user.location, 'driving')
        #     if distance <= cur_user.max_match_distance:
        #         distance_append = {"match_user_username": user.username,
        #                            "distance": distance}
        #         distances.append(distance_append)
        # sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        right_swipes = self.right_swipe_matches(user_location, current_user_id)
        profile_matches = self.profile_recommendations(user_location, current_user_id)

        print ("***************************")
        print (right_swipes)
        print ("***************************")
        print(profile_matches)
        print ("***************************")

        return right_swipes+profile_matches

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
    def profile_recommendations(self, user_location, current_user_id):
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
            elif (Right_Swipe.query.filter_by(target_id=current_user_id).filter_by(swiper_id=user.id).first()) is not None:
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
            if distance == -1:
                print("Google Maps could not return a possible distance. Check the error message from Google")
                exit(300)
            if distance <= cur_user.max_match_distance:
                distance_append = {"match_user_username": user.username,
                                   "distance": distance}
                distances.append(distance_append)
        sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        return sorted_distances

    def right_swipe_matches(self, user_location, current_user_id):
        #current_user_id = current_user.id
        user = User_Profile()
        all_right_swipes = Right_Swipe.query.filter_by(target_id=current_user_id).all()
        cur_user = User_Profile.query.filter_by(id=current_user_id).first()
        cur_user_sexuality = cur_user.gender_preference.name
        cur_user_min_age = cur_user.min_match_age
        cur_user_max_age = cur_user.max_match_age
        distances = []
        for right_swipe in all_right_swipes:
            potential_right = User_Profile.query.filter_by(id=right_swipe.swiper_id).first()
            user_age = self.calculateAge(potential_right.dob)
            if potential_right.username == cur_user.username:
                continue
            elif right_swipe.became_match == True:
                continue
            elif potential_right.gender.name != cur_user_sexuality:
                print (potential_right.gender)
                continue
            elif potential_right.gender_preference.name != cur_user.gender.name:
                continue
            elif user_age < cur_user_min_age:
                continue
            elif user_age > cur_user_max_age:
                continue
            distance = self.Google_Maps_Api.get_distance(user_location, potential_right.location, 'driving')
            if distance <= cur_user.max_match_distance:
                distance_append = {"match_user_username": potential_right.username,
                                   "distance": distance}
                distances.append(distance_append)
        sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        return sorted_distances

class Right_Swipes:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)

    def right_swipes(self, match_dict, current_user_id, target_id):
        # current_user_id = 1
        # target_id=User_Profile.query.filter_by(username=match_dict['match_user_username']).first().id
        first_right_swipe = Right_Swipe.query.filter_by(swiper_id=target_id).filter_by(target_id=current_user_id).first()
        if first_right_swipe is not None:
            first_right_swipe.became_match = True
            db.session.commit()
            return 1
        else:
            return -1



