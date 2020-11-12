import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.getcwd() + '/../../'))

from backend.server.simulation import app, signup, login, current_user, logout


class TestSignup(unittest.TestCase):
    with app.app_context():
        print("Testing authentication:")
        command = ""
        while True:
            command = input("commands: signup, login, logout, exit: ")
            if command == "exit":
                break

            if command == "get user":
                print(current_user.cu)
                continue

            if command == "signup":
                request = {'email': input("enter email: "), 'username': input("enter username: "),
                           'f_name': input("enter first name: "), 'l_name': input("enter last name: "),
                           'password': input("enter password: "), 'password_repeat': input("confirm password: "),
                           'dob': input("enter DOB (YYYY-MM-DD): "), 'min_target': input("enter min matching age: "),
                           'max_target': input("enter max matching age: "),
                           'gender': input("enter gender (male, female, other): "),
                           'gender_preference': input("enter gender preference (male, female, everyone): "),
                           'bio': input("enter bio: "), 'location': input("enter matching location: "),
                           'max_match_distance': input("enter max match distance: ")}

                request = {'email': 'sascha.graham@gmail.com', 'username': 'sascha', 'f_name': 'sascha',
                           'l_name': 'graham', 'password': 'awd', 'password_repeat': 'awd', 'dob': '1999-11-02',
                           'min_target': '16', 'max_target': '22', 'gender': 'male', 'gender_preference': 'everyone',
                           'bio': 'awd', 'location': '23 Cameron Ave Artarmon', 'max_match_distance': '200'}

                signup(request)
                continue

            if command == "login":
                request = {'username': input("enter username: "), 'password': input("enter password: ")}

                login(request)
                continue

            if command == "logout":

                logout()
                continue



