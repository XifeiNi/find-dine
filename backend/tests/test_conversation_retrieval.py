import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.app import app
from backend.server.models import User_Profile, Right_Swipe, db
from flask import Flask, render_template, session

import unittest
from backend.Classes.message_system import Message_System
from flask import session, Flask
import datetime
from datetime import date, datetime


class TestMessageSystem(unittest.TestCase):

    def test_message_system(self):
        message_sys = Message_System()
        with app.app_context():
            conversations = message_sys.getConversations()
            for conversation in conversations:
                print("########################")
                # print("First Name: ", recommendation.f_name)
                # print ("Last Name: ", recommendation.l_name)
                # print("addr: ", event.addr)
                # print("start: ", event.start_time)
                # print("end: ", event.end_time)
                print("Username: ", conversation['username'])
                print("Last_Message: ", conversation['last_message'])
                print ("Time: ", conversation['time'])

    def test_conversation_system(self):

        room_id = "6+3"
        message_sys= Message_System()
        with app.app_context():
            conversation, messages= message_sys.getMessages(room_id)
            print("########################")
            print("Username: ", conversation['conversation_username'])
            print ("***********************")
            for message in messages:
                print("########################")
                # print("First Name: ", recommendation.f_name)
                # print ("Last Name: ", recommendation.l_name)
                # print("addr: ", event.addr)
                # print("start: ", event.start_time)
                # print("end: ", event.end_time)
                print("Message Sender: ", message['message_username'])
                print("Message: ", message['message'])
                print ("Time: ", message['time_sent'])

        #assert False