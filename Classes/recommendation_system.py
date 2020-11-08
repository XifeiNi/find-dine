from flask_login import current_user
from .google_maps import Google_Maps
from ..business.models import Business_Profile
from flask import Flask, render_template, session
import datetime
from datetime import datetime as dt

GOOGLE_MAPS_API_KEY = "AIzaSyDNSQlkoM44anY1fYWt-c84gFf_2S40lbg"

class Recommendation_System:

    def __init__(self):
        self.Google_Maps_Api = Google_Maps(GOOGLE_MAPS_API_KEY)
    def getRecommendations(self, user_location):
        id = current_user.id
        all_users = Business_Profile.query.all()
        for user in all_users:


