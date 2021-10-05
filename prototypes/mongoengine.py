from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError
#========================
#This file was made using a mongoengine tutorial
#========================

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bhealth"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def home_page():
    online_users = db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)
        
        #finds page or returns 404 instead of crashing
@app.route("/user/<username>")
def user_profile(username):
    user = db.users.find_one_or_404({"_id": username})
    return render_template("user.html",
        user=user)

@app.route("/add_one")
def add_one():
    db.todos.insert_one({
        'username': "chris",
        'password': "000",
        'height' : 200,
        'weight' : 83})
    return jsonify(message="success")

@app.route("/add_many")
def add_many():
    try:
        todo_many = db.todos.insert_many([
            {'_id': 1, 'username': "im number one ", 'password': "passwordone ", 'height': 20, 'weight': 350},
            {'_id': 8, 'username': "im number two", 'password': "passwordtwo", 'height': 30, 'weight': 400},
            {'_id': 2, 'username': "im number three", 'password': "passwordthree", 'height': 40, 'weight': 500},
            {'_id': 9, 'username': "im number four", 'password': "passwordfour", 'height': 50, 'weight': 40},
            {'_id': 10, 'username': "im number five", 'password': "passwordfive", 'height': 60, 'weight': 30},
            {'_id': 5, 'username': "im number six", 'password': "passwordsix", 'height': 70, 'weight': 30},
        ], ordered=False)
    except BulkWriteError as e:
        return jsonify(message="duplicates encountered and ignored",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return jsonify(message="success", insertedIds=todo_many.inserted_ids)