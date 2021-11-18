from flask import Flask, redirect, url_for, render_template, request, session
from flask.ctx import has_request_context
from flask_session import Session
import secrets
import json
import requests

#key = ""
global key
global CURRENT_USER
#key = "f602c24d536945e6b0a9d94748614609"
key = "6b34aa15afef46d29e32d0c5adf63cd6"
#key =  "f6333c76ce7148d4b3b22172e8267b65"

secret = secrets.token_urlsafe(16)
app = Flask(__name__)
from database import *
from calorie_api import *

sess = Session()
app.config['SESSION_TYPE'] = 'mongodb'
app.config["SECRET_KEY"] = secret
app.config.from_object(__name__)

users = db_getUsersTable()
history = db_getHistoryTable()

CURRENT_USER = None

'''
    Main python app that runs the flask server and loads html pages.
    All logic should be sent to other .py files for processing
'''

@app.route('/')
def home():
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

@app.route('/testing_workout')
def workout():
    return render_template("testing_workout.html")


@app.route('/testing_profilepic')
def profilepic():
    return render_template("testing_profilepic.html")

@app.route('/testing_password')
def password():
    return render_template("testing_password.html")

@app.route('/test_notifications')
def notification():
    return render_template("test_notifications.html")

@app.route('/testing_username')
def username():
    return render_template("testing_username.html")
    

def strip(text):
 text= text.replace("<ol>","").replace("<li>","").replace("</li>","").replace("</ol>","").replace("<b>","").replace("</b>","").replace("<a>","").replace("</a>","").replace("<a href=","").replace(">","").replace(";","")
 return text

@app.route('/testing_recipes', methods = ['GET','POST'])
def recipes():
   response = requests.get("https://api.spoonacular.com/recipes/636243/information?includeNutrition=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642178/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664080/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/testing_recipes"
   href2 = "/a/"
   href3 = "/a2/"
   title = "American"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/a/', methods = ['GET','POST'])
def recipiesA2():
   response = requests.get("https://api.spoonacular.com/recipes/636243/information?includeNutrition=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642178/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664080/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/testing_recipes"
   href2 = "/a/"
   href3 = "/a2/"
   title = "American"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/a2/', methods = ['GET','POST'])
def recipiesA3():
   response = requests.get("https://api.spoonacular.com/recipes/636243/information?includeNutrition=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642178/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664080/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/testing_recipes"
   href2 = "/a/"
   href3 = "/a2/"
   title = "American"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/french/',methods=['GET','POST'])
def recipiesF1():
   response = requests.get("https://api.spoonacular.com/recipes/650239/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648641/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664689/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/french/"
   href2 = "/french2/"
   href3 = "/french3/"
   title = "French"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/french2/',methods=['GET','POST'])
def recipiesF2():
   response = requests.get("https://api.spoonacular.com/recipes/650239/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648641/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664689/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/french/"
   href2 = "/french2/"
   href3 = "/french3/"
   title = "French"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/french3/',methods=['GET','POST'])
def recipiesF3():
   response = requests.get("https://api.spoonacular.com/recipes/650239/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648641/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/664689/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/french/"
   href2 = "/french2/"
   href3 = "/french3/"
   title = "French"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/japanese/',methods=['GET','POST'])
def recipiesJ1():
   response = requests.get("https://api.spoonacular.com/recipes/1590307/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648500/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/660493/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/japanese/"
   href2 = "/japanese2/"
   href3 = "/japanese3/"
   title = "Japanese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/japanese2/',methods=['GET','POST'])
def recipiesJ2():
   response = requests.get("https://api.spoonacular.com/recipes/1590307/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648500/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/660493/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/japanese/"
   href2 = "/japanese2/"
   href3 = "/japanese3/"
   title = "Japanese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/japanese3/',methods=['GET','POST'])
def recipiesJ3():
   response = requests.get("https://api.spoonacular.com/recipes/1590307/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/648500/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/660493/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/japanese/"
   href2 = "/japanese2/"
   href3 = "/japanese3/"
   title = "Japanese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/chinese/',methods=['GET','POST'])
def recipiesC1():
   response = requests.get("https://api.spoonacular.com/recipes/644826/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/918033/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/969270/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/chinese/"
   href2 = "/chinese2/"
   href3 = "/chinese3/"
   title = "Chinese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/chinese2/',methods=['GET','POST'])
def recipiesC2():
   response = requests.get("https://api.spoonacular.com/recipes/644826/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/918033/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/969270/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/chinese/"
   href2 = "/chinese2/"
   href3 = "/chinese3/"
   title = "Chinese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/chinese3/',methods=['GET','POST'])
def recipiesC3():
   response = requests.get("https://api.spoonacular.com/recipes/644826/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/918033/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/969270/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/chinese/"
   href2 = "/chinese2/"
   href3 = "/chinese3/"
   title = "Chinese"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/spanish/',methods=['GET','POST'])
def recipiesS1():
   response = requests.get("https://api.spoonacular.com/recipes/660868/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/1095794/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/632706/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/spanish/"
   href2 = "/spanish2/"
   href3 = "/spanish3/"
   title = "Spanish"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/spanish2/',methods=['GET','POST'])
def recipiesS2():
   response = requests.get("https://api.spoonacular.com/recipes/660868/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/1095794/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/632706/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/spanish/"
   href2 = "/spanish2/"
   href3 = "/spanish3/"
   title = "Spanish"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/spanish3/',methods=['GET','POST'])
def recipiesS3():
   response = requests.get("https://api.spoonacular.com/recipes/660868/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/1095794/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/632706/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/spanish/"
   href2 = "/spanish2/"
   href3 = "/spanish3/"
   title = "Spanish"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/italian/',methods=['GET','POST'])
def recipiesI1():
   response = requests.get("https://api.spoonacular.com/recipes/636910/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642722/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/658544/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/italian/"
   href2 = "/italian2/"
   href3 = "/italian3/"
   title = "Italian"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/italian2/',methods=['GET','POST'])
def recipiesI2():
   response = requests.get("https://api.spoonacular.com/recipes/636910/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642722/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/658544/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/italian/"
   href2 = "/italian2/"
   href3 = "/italian3/"
   title = "Italian"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/italian3/',methods=['GET','POST'])
def recipiesI3():
   response = requests.get("https://api.spoonacular.com/recipes/636910/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/642722/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/658544/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/italian/"
   href2 = "/italian2/"
   href3 = "/italian3/"
   title = "Italian"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/european/',methods=['GET','POST'])
def recipiesE1():
   response = requests.get("https://api.spoonacular.com/recipes/715495/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/658515/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/644885/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data['instructions'])
   DSumm1 = strip(data['summary'])
   href1 = "/european/"
   href2 = "/european2/"
   href3 = "/european3/"
   title = "European"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/european2/',methods=['GET','POST'])
def recipiesE2():
   response = requests.get("https://api.spoonacular.com/recipes/715495/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/658515/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/644885/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data2['instructions'])
   DSumm1 = strip(data2['summary'])
   href1 = "/european/"
   href2 = "/european2/"
   href3 = "/european3/"
   title = "European"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)

@app.route('/european3/',methods=['GET','POST'])
def recipiesE3():
   response = requests.get("https://api.spoonacular.com/recipes/715495/information?includeInstructions=true&apiKey=" + key)
   response2 = requests.get("https://api.spoonacular.com/recipes/658515/information?includeInstructions=true&apiKey=" + key)
   response3 = requests.get("https://api.spoonacular.com/recipes/644885/information?includeInstructions=false&apiKey=" + key)
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   DInstruc1 = strip(data3['instructions'])
   DSumm1 = strip(data3['summary'])
   href1 = "/european/"
   href2 = "/european2/"
   href3 = "/european3/"
   title = "European"
   return render_template("testing_recipes.html",DInstruc1 = DInstruc1,DSumm1=DSumm1, data = data ,data2 = data2,data3 = data3,href1 = href1,href2 = href2,href3 = href3,title = title)


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
            db_set_current_user(CURRENT_USER)
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
            verify_update = db_update_settings(settings)
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
        username = request.form.get("username")
        password = encrypt_password(request.form.get("password"))
        weight = request.form.get("weight")
        height = request.form.get("height")
        activity_level = request.form.get("activity_level")
        gender = request.form.get("gender")
        dob = request.form.get("dob")
        diet = request.form.get("diet")
        new_user = {
            "username": username,
            "password": password,
            "weight": weight,
            "height": height,
            "activity_level": activity_level,
            "diet": diet,
            "gender": gender,
            "dob": dob
        }
        

        if(users.count_documents({"username" : request.form.get("username")}) == 0) :
            users.insert_one(new_user)
            session['username'] = username
            CURRENT_USER = users.find_one({'username': username})
            CURRENT_USER_ID = CURRENT_USER["_id"]
            new_user_hist = {
                "_id": CURRENT_USER_ID,
                "calorie_goal": 0,
                "water_goal": 0,
                "eaten_cals": 0,
                "water_tracked": 0,
                "workout_cals": 0,
                "last_workout": "None",
                "weight_goal": 0,
                "linked": False
            }
            
            history.insert_one(new_user_hist)
            print(history.find_one({"_id": CURRENT_USER_ID}))

            db_set_default_calorie_goal(weight, height, activity_level, gender, dob, CURRENT_USER_ID),
            db_update_water_goal(64,CURRENT_USER_ID),
            db_update_eaten_cals(0,CURRENT_USER_ID),
            db_update_water_tracked(0,CURRENT_USER_ID),
            db_update_workout_cals(0,CURRENT_USER_ID),
            db_update_last_workout("None",CURRENT_USER_ID),
            db_update_weight_goal(0,CURRENT_USER_ID),
            db_update_linked(True,CURRENT_USER_ID)

            print(history.find_one({"_id": CURRENT_USER_ID}))
            
            db_set_current_user(CURRENT_USER)
            return render_template("testing_homepage.html", curr_user=CURRENT_USER)
        else:
            return "That login information is already taken!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')

@app.route('/calorie', methods=['GET', 'POST'])
def index():
    username = session['username'] 
    CURRENT_USER = users.find_one({'username': username})
    CURRENT_USER_ID = CURRENT_USER["_id"]
    if request.method == "GET":
        db_set_current_user(CURRENT_USER)
        #CURRENT_USER works here
        user_hist = history.find_one({"_id":CURRENT_USER_ID})
        print(user_hist)
        cal_goal = user_hist["calorie_goal"]
        cals_consumed = user_hist["eaten_cals"]
        cals_remaining =cal_goal-cals_consumed
        #ingredient = request.form['ingredient']
        #cals = calorie_calc(ingredient)
        return render_template('calorie.html', calorie_goal=cal_goal, cals=0, cals_consumed=cals_consumed, cals_remaining=cals_remaining)
        #return render_template('calorie.html', ingredient=ingredient, cals=cals, calorie_goal=cal_goal)
    # else:
        # return render_template('calorie.html')
    elif request.method == "POST":
        user_hist = history.find_one({"_id": CURRENT_USER_ID})
        cal_goal = user_hist["calorie_goal"]
        ingredient = request.form['ingredient']
        cals = calorie_calc(ingredient)
        if cals == "Invalid Entry: Check spelling and format":
            return render_template('calorie.html', ingredient=ingredient, cals=cals, cals_consumed=cals, calorie_goal=cal_goal, cals_remaining=cals)
        db_update_eaten_cals(cals, CURRENT_USER_ID)
        cals_consumed = user_hist["eaten_cals"]
        cals_remaining =cal_goal-cals_consumed
        return render_template('calorie.html', ingredient=ingredient, cals=cals, cals_consumed=cals_consumed, calorie_goal=cal_goal, cals_remaining=cals_remaining)
    #else:
       # return render_template('calorie.html')


        
#def index():
  #  print("5")
   # curr_user = CURRENT_USER
  #  user_hist = history.find_one({"_id": curr_user["_id"]})
   # cal_goal = user_hist["calorie_goal"]
   # print("6")
   # return render_template('calorie.html', calorie_goal=cal_goal)

if __name__ == "__main__":
    app.run(debug=True)
