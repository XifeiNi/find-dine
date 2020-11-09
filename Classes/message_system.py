import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from flask_login import current_user
from .google_maps import Google_Maps
from find_dine.server.models import User_Profile, Conversation, Messages, db
# from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt


class Message_System:

    def getConversations(self):
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

        username_one_rooms = Conversation.query.filter_by(username_one=current_user_id).all()
        username_two_rooms = Conversation.query.filter_by(username_two=current_user_id).all()
        for username_one_room in username_one_rooms:

            

        return right_swipes+profile_matches





