from flask_login import current_user
from .google_maps import Google_Maps
from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import datetime as dt

GOOGLE_MAPS_API_KEY = "AIzaSyDNSQlkoM44anY1fYWt-c84gFf_2S40lbg"

class Recommendation_System:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def getRecommendations(self, user_location):
        current_username = session['current_username']
        all_users = User_Profile.query.filter
        distances = []
        for user in all_users:
            if user.username == current_username:
                continue
            distance = self.Google_Maps_Api.get_distance(user_location, user.location, 'driving')
            distance_append = {"match_user.username": user.username,
                               "distance": distance}
            distances.append(distance_append)
        sorted_distances = sorted(distances, key=lambda dict: dict['distance'])
        return sorted_distances




