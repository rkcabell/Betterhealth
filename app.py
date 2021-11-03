from flask import Flask, redirect, url_for, render_template, request, session
from flask.ctx import has_request_context
from flask_session import Session
import secrets

secret = secrets.token_urlsafe(16)
app = Flask(__name__)
from database import *

sess = Session()
app.config['SESSION_TYPE'] = 'mongodb'
app.config["SECRET_KEY"] = secret
app.config.from_object(__name__)

CURRENT_USER = None

users = db_getUsersTable()
history = db_getHistoryTable()
'''
    Main python app that runs the flask server and loads html pages.
    All logic should be sent to other .py files for processing
'''

@app.route('/')
def home():
    return render_template("testing_homepage.html")

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



@app.route('/login', methods=["GET", "POST"])
def login():
    # if user hits submit button
    if request.method == "POST":
        if request.form.get('submitbutton') == 'signin':
            username = request.form.get("username")
            password = request.form.get("password")
            verify_login = db_login(username, password)
            if verify_login == False:
                return "Invalid login information"
            # Set user to CURRENT USER
            session['username'] = username
            CURRENT_USER = users.find_one({'username': username})
            # pass current user into homepage
            return render_template("testing_homepage.html", curr_user=CURRENT_USER)
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
    return render_template("login.html")

# Loads page
# when form is submitted, update user and reload page
@app.route('/settings', methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        if 'username' in session:
            curr_user = users.find_one({'username': session['username']})
            weight = request.form.get("input_weight")
            height = request.form.get("input_height")
            dob = request.form.get("input_dob")
            # value = female, male, other
            if 'gender' in request.form:
                gender = request.form['gender']
            else:
                gender = None
            # value = sedentary, light, moderate, heavy
            if 'activity' in request.form:
                activity_level = request.form['activity']
            else:
                activity_level = None
            # value = regular, vegan, vegetarian
            if 'diet' in request.form:
                diet = request.form['diet']
            else:
                diet = None

            settings = [weight, height, dob, gender, activity_level, diet]
            print(session)
            verify_update = db_update_settings(settings, curr_user)
            print("Update succeeded: " + str(verify_update))
            return render_template("settings.html")
        # username not in session, return to login
        else:
            return render_template("login.html")
    # load settings when form not submitted
    else:
        return render_template("settings.html")

      
@app.route('/register_form', methods=["GET", "POST"])
def register_form():
    if request.method == "POST":
        new_user = {
            "username": request.form.get("username"),
            "password": encrypt_password(request.form.get("password")),
            "weight": request.form.get("weight"),
            "height": request.form.get("height"),
            "activity_level": request.form.get("activity_level"),
            "diet": request.form.get("diet"),
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob")
        }
        if(users.count_documents({"username" : request.form.get("username")}) == 0 and users.count_documents({"password" : request.form.get("password")}) == 0):
            users.insert_one(new_user)
            return render_template("testing_homepage.html")
        else:
            return "That login information is already taken!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('/login')

if __name__ == "__main__":
    app.run(debug=True)
