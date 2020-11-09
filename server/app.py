# from flask import Flask, render_template, session
# from flask_socketio import SocketIO, send, emit, join_room, leave_room
#
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
#
# # @app.route('/login')
# # def login():
# #     check password - assuming thats fine
# #     session['user'] = database.get("username")
#
# @app.route('/')
# def startup():
#     return """
#      <!DOCTYPE html>
#     <script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
# <script type="text/javascript" charset="utf-8">
#     var socket = io();
#     socket.on('connect', function() {
#         socket.emit('join', {username: 'You\\'re fucked''});
#     });
# </script>
#     """
#
# # @app.route('/logout')
# # def logout():
# #     session.clear()
#
# @socketio.on('connect')
# def handle_message():
#     print('someone connected')
#
# @socketio.on('message')
# def handle_message(message):
#     room = session['room']
#     send(message, room=room)
#
# @socketio.on('join')
# def on_join(data):
#     # username = session['user'].get('username')
#     # room = username + data['other']
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     session['room'] = room
#     send('Oi dickhead, join this room ' + room)
#     send(username + ' has entered the room.', room=room)
#     send('blah', room='qwer')
#     emit('message', 'blah', room='qwer')
#
# @socketio.on('leave')
# def on_leave(data):
#     # username = session['user'].get('username')
#     # room = username + data['other']
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)
#
# if __name__ == '__main__':
#     socketio.run(app)

from flask import Flask, render_template, jsonify, request, abort
from flask_socketio import SocketIO, join_room
from flask_sqlalchemy import SQLAlchemy
from models import *  # Conversation, Messages, db
from datetime import datetime, date

# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_jsglue import JSGlue
# from config import Config
#
# # Extension Initialisation
# bootstrap = Bootstrap()
# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# jsglue = JSGlue()
#
# # Factory Function
# def create_app():
#     # Create Flask Instance
#     app = Flask(__name__, static_url_path='/static')
#     app.config.from_object(Config)
#
#     # Apply Extension to Flask Instance
#     bootstrap.init_app(app)
#     db.init_app(app)
#     login_manager.init_app(app)
#     jsglue.init_app(app)
from server.models import all_businesses_list

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'user_side#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
app.config['JSON_SORT_KEYS'] = False
db.init_app(app)
socketio = SocketIO(app)

with app.app_context():
    db.create_all()


@app.route('/')
def sessions():
    return render_template('index.html')


def messageReceived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    room = 'test_room'
    message = Messages(room=room,
                       sender_username=json['user_name'],
                       time_sent=datetime.now().time(),
                       date_sent=datetime.today().date(),
                       message=json['message'])
    db.session.add(message)
    db.session.commit()
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('join')
def on_join():
    # username = session['user'].get('username')
    # room = username + data['other']
    # username = data['username']
    room = 'test_room'
    join_room(room)
    exists = (Conversation.query.filter_by(room=room).first())
    if exists is None:
        conversation = Conversation(room=room)
        db.session.add(conversation)
        db.session.commit()


@app.route('/businesses', methods=['GET'])
def business_list():
    if request.method == 'GET':
        result = all_businesses_list()
        for item in result:
            # instance = db.session.query(Business_Profile).filter_by(id=item["id"]).first() is not None
            instance = db.session.query(Business_Profile).filter_by(id=item["id"]).first()
            if not instance:
                print(item["id"], item["name"])
                business = Business_Profile(id=int(item["id"]),
                                            name=item["name"],
                                            email=item["email"],
                                            description=item["description"],
                                            address=item["address"],
                                            price_guide=item["price_guide"],
                                            category=item["category"])
                db.session.add(business)
                db.session.commit()
        list_of_buinesses = db.session.query(Business_Profile).all()

    # return jsonify(all_businesses_list())
    return render_template('business_list.html', list=list_of_buinesses)


@app.route('/businesses/<b_id>', methods=['GET'])
def deals_info(b_id):
    # info = deals_info(str(b_id))
    print(b_id)
    #deals_info = db.session.query(Deals).filter_by(business_id=b_id)
    #print(deals_info)
    #return jsonify(deals_info)
    return()


@app.route('/deals', methods=['GET'])
def deals_list():
    if request.method == 'GET':

        result = all_deals_list()

        for item in result:
            instance = db.session.query(Deals).filter_by(id=item["id"]).first()
            if not instance:
                # print(item["id"], item["deal_name"])
                date_c = datetime.strptime(item["date_created"], '%Y-%m-%d')
                date_e = datetime.strptime(item["date_expiry"], '%Y-%m-%d')
                deals = Deals(id=int(item["id"]),
                              business_id=item["business_id"],
                              deal_name=item["deal_name"],
                              description=item["description"],
                              discount_percentage=item["discount_percentage"],
                              date_created=date_c,
                              date_expiry=date_e)
                db.session.add(deals)
                db.session.commit()
            # else:
            # print(item["id"], item["description"])
    # return jsonify(all_deals_list())
    return render_template('deals.html', list=result)


if __name__ == '__main__':
    socketio.run(app, debug=False)
