from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

#from database import dblogin

import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import ReturnDocument

'''
    Main python app that runs the flask server and loads html pages.
    All logic should be sent to other .py files for processing
'''

# Home page

client = MongoClient()
db = client.bhealth
users = db.users
history = db.history

@app.route('/')
def home():
    return render_template("testing_homepage.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/testing_homepage')
def homepage():
    return render_template("testing_homepage.html")

@app.route('/profile_setup')
def profile():
    return render_template("profile_setup.html")

@app.route('/testing_recipes')
def recipes():
    return render_template("testing_recipes.html")




@app.route('/handle_form', methods=["GET", "POST"])
def handle_form():
    # Testing get form data
    if request.method == "POST":
        if request.form.get('submitbutton') == 'signin':
            # name = email in HTML form under login page
            username = request.form.get("username")
            # password
            password = request.form.get("password")
            #return "Your name is " + username + " and your password is " + password
            #if dblogin(username, password) != "None":
            #doc = users.find_one({"username" : username})
            if users.find_one({"username" : username}) == users.find_one({"password" : password}) and users.count_documents({"username" : username}) > 0 and users.count_documents({"password" : password}) > 0:
                return render_template("testing_homepage.html")
            else:
                #users.delete_many({ "username": {"$regex": "^w"} })
                #for data in users.find():
                #    print(data)
                return "Invalid login information"
        elif request.form.get('submitbutton') == 'register':
            #new_user = {
            #    "username": request.form.get("username"),
            #    "password": request.form.get("password"),
            #    "weight": 0,
            #    "height": 0,
            #    "activity_level": "SEDENTARY",
            #    "diet": "NO_RESTRICTIONS",
            #    "gender": "OTHER",
            #    "dob": "1970-01-01"
            #}
            #users.insert_one(new_user)
            return render_template("register.html")

# For json data EXAMPLE

@app.route('/register_form', methods=["GET", "POST"])
def register_form():
    if request.method == "POST":
        new_user = {
            "username": request.form.get("username"),
            "password": request.form.get("password"),
            "weight": request.form.get("weight"),
            "height": request.form.get("height"),
            "activity_level": request.form.get("activity_level"),
            "diet": request.form.get("diet"),
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob")
        }
        users.insert_one(new_user)
        return render_template("testing_homepage.html")


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return ''

# pass in page as var


# @app.route('/<name>/')
# def user(name):
#     return render_template("index.html", content=[name])


if __name__ == "__main__":
    app.run(debug=True)
