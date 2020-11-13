import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from flask_login import current_user
from .google_maps import Google_Maps
from backend.server.models import User_Profile, Conversation, Messages, Match, db
# from ..server.models import User_Profile
from flask import Flask, render_template, session
import datetime
from datetime import date
from datetime import datetime as dt


class Message_System:

    def getConversations(self, current_user_id):
        #current_user_id = current_user.id
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
        conversations = []
        for username_one_room in username_one_rooms:
            user_two = User_Profile.query.filter_by(id=username_one_room.username_two).first()
            if user_two is None:
                print ("Something is wrong, username 2 doesnt exist")
                return -1
            username = user_two.f_name + " " + user_two.l_name
            messages = Messages.query.filter_by(room=username_one_room.room).order_by(Messages.time_sent.desc()).all()
            if messages is not None and len(messages) > 0:
                last_message_record = messages[0]
                last_message = messages[0].message
                time = last_message_record.time_sent
            else:
                last_message = "Congrats, you are starting a new relationship with " + username
                conversation_match = Match.query.filter_by(conversation_id=username_one_room.room).first()
                if conversation_match is None:
                    print ("Something is wrong, the Match doesnt exist")
                    return -2
                time = conversation_match.created
            conversation = {"username": username,
                            "last_message": last_message,
                            "time": time}
            conversations.append(conversation)

        for username_two_room in username_two_rooms:
            user_one = User_Profile.query.filter_by(id=username_two_room.username_one).first()
            if user_one is None:
                print ("Something is wrong, username 2 doesnt exist")
                return -1
            username = user_one.f_name + " " + user_one.l_name
            messages = Messages.query.filter_by(room=username_two_room.room).order_by(Messages.time_sent.desc()).all()
            if messages is not None and len(messages) > 0:
                last_message_record = messages[0]
                last_message = messages[0].message
                time = last_message_record.time_sent
            else:
                last_message = "Congrats, you are starting a new relationship with " + username
                conversation_match = Match.query.filter_by(conversation_id=username_two_room.room).first()
                if conversation_match is None:
                    print("Something is wrong, the Match doesnt exist")
                    return -2
                time = conversation_match.created
            conversation = {"username": username,
                            "last_message": last_message,
                            "time": time}
            conversations.append(conversation)
        sorted_conversations = sorted(conversations, key=lambda dict: dict['time'])

        return sorted_conversations

    def getMessages(self, room_id, current_user_id):
        conversation = Conversation.query.filter_by(room=room_id).first()
        if conversation is None:
            print ("Something is wrong, conversation doesnt seem to exist")
            return -1
        username_one = conversation.username_one
        username_two = conversation.username_two
        username_name = ""
        if username_one == current_user_id:
            username = User_Profile.query.filter_by(id=username_two).first()
            if username is None:
                print ("Something is wrong, user_one of conversation doesnt exist")
                return -2
            username_name = username.f_name + " " + username.l_name
        elif username_two == current_user_id:
            username = User_Profile.query.filter_by(id=username_one).first()
            if username is None:
                print ("Something is wrong, user_two of conversation doesnt exist")
                return -3
            username_name = username.f_name + " " + username.l_name
        else:
            print ("Something is wrong, none of the users is the current user")
            return -4

        messages = Messages.query.filter_by(room=room_id).order_by(Messages.time_sent.asc()).all()
        conversation_messages = []
        for message in messages:
            sender = User_Profile.query.filter_by(id=message.sender_username).first()
            sender_name = sender.f_name + " "+ sender.l_name
            if sender is None:
                print ("Something is wrong, sender doesnt exist")
                return -5
            conversation_message = {"message_username": sender_name,
                                    "message": message.message,
                                    "time_sent": message.time_sent}
            conversation_messages.append(conversation_message)
        sorted_conv_messages = sorted(conversation_messages, key=lambda dict: dict['time_sent'])


        conversation_detail={"conversation_username": username_name}
        return conversation_detail, sorted_conv_messages




