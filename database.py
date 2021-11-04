# https://pymongo.readthedocs.io/en/stable/tutorial.htmly
# see link for
# bulk inserts, bulk querying, count num of documents,
# advanced queries, indexing(ascending)

from flask.globals import current_app
from flask.templating import render_template
import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from pass_sec import encrypt_password, check_encrypted_password
from datetime import datetime

CURRENT_USER = None
CURRENT_USER_ID = None


# Constants for 'activity_level' in bhealth.users.activity_level
SEDENTARY = 0
LIGHT = 1
MODERATE = 2
HEAVY = 3

# Constants for 'diet' in bhealth.users.diet
NO_RESTRICTIONS = 0
VEGETARIAN = 1
VEGAN = 2

# Constants for 'gender' in bhealth.users.gender
FEMALE = 0
MALE = 1
OTHER = 2


# For default host, port
client = MongoClient()
print("client:", client)

db = client.bhealth
users = db.users
history = db.history


def db_getUsersTable():
    return db.users

def db_getHistoryTable():
   return db.history

def db_get_current_user(curr_user):
    global CURRENT_USER
    global CURRENT_USER_ID
    CURRENT_USER = curr_user
    CURRENT_USER_ID = curr_user['_id']
########################################## LOGIN ##########################################

# Finds a doc in the database such that password matches for given username
# returns true if user exists, otherwise false
def db_login(username, password):
    login_attempt = {"username": username}
    user_found = users.find_one(login_attempt)
    print("\nAttempting to log into: " + str(login_attempt))
    if user_found is None:
        print("That user doesn't exist")
        return False
    real_pass = user_found["password"]
    if check_encrypted_password(password, real_pass):
        print("password check passed")
        return True
    print("password check failed")
    return False

########################################## SETTINGS UPDATES ##########################################

# update the settings applied on settings page
# Parameters: list of updated settings from app.py
# Returns: list of only the settings that were nonempty
def db_update_settings(settings):
    if CURRENT_USER is not None:
        CURRENT_USER_ID = CURRENT_USER['_id']
    else:
        print("CURRENT_USER: " + str(CURRENT_USER))
        return False
    updated_settings = []
    setting_elems = ["weight", "height", "dob", "gender", "activity", "diet"]
    print("Inputted settings: " + str(settings))
    # make string settings into constants
    settings = assign_constants(settings)
    for i in range(len(settings)):
        if (settings[i] is not None):
            users.find_one_and_update({"_id": CURRENT_USER_ID},
            {"$set": {setting_elems[i] : settings[i]}})
            # store updated settings to return
            updated_settings.append(settings[i])
    print("Changed settings: " + str(updated_settings))
    return updated_settings

# make the settings into the proper constant names
def assign_constants(settings):
    for x in settings:
        if(x == "sedentary"):
            x = SEDENTARY
        elif(x == "light"):
            x = LIGHT
        elif(x == "moderate"):
            x = MODERATE
        elif(x == "heavy"):
            x = HEAVY

        if(x == "female"):
            x = FEMALE
        elif(x == "male"):
            x = MALE
        elif(x == "other"):
            x = OTHER

        if(x == "regular"):
            x = NO_RESTRICTIONS
        elif(x == "vegan"):
            x = VEGAN
        elif(x == "vegetarian"):
            x = VEGETARIAN
    return settings

def db_register():
    return False

def db_update_history():
    return 
    False
########################################## HISTORY TABLE UPDATES ##########################################
# takes int
def db_update_calorie_goal(x):
    curr_calorie_goal = history.find_one({"_id": CURRENT_USER_ID})['calorie_goal']
    if curr_calorie_goal is None:
        user = users.find_one({"_id": CURRENT_USER_ID})
        gender = user['gender']
        weight = user['weight']
        height = user['height']
        activity_level = user['activity_level']
        dob = user['dob'].split("-")
        age = get_age(dob)

        # FEMALE
        # 655 + (9.6 X weight in kg) + (1.8 x height in cm) – (4.7 x age in yrs)
        if gender == 0:
            x = 655 + (9.6 + weight) + (1.8 * height) - (4.7 * age)
        # MALE OR OTHER
        # 66 + (13.7 X weight in kg) + (5 x height in cm) – (6.8 x age in yrs)
        elif gender == 1 or gender == 2:
            x = 66 + (13.7 + weight) + (5 * height) - (6.8 * age)

        if activity_level == 0:
            x *= 1.2
        elif activity_level == 1: 
            x *= 1.375
        elif activity_level == 2: 
            x *= 1.55
        elif activity_level == 3: 
            x *= 1.725

    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"calorie_goal" : x}})

# takes int
def db_update_water_goal(x):
    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"water_goal" : x}})

# takes int
def db_update_water_tracked(x):
    curr_water_tracked = history.find_one({"_id": CURRENT_USER_ID})['water_tracked']
    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"water_tracked" : x + curr_water_tracked}})

# only increases, to decrease use workout
def db_update_eaten_cals(x):
    curr_eaten_cals = history.find_one({"_id": CURRENT_USER_ID})['eaten_cals']
    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"eaten_cals" : x + curr_eaten_cals}})

# only increases, this number is subtracted from eaten to show daily cals
def db_update_workout_cals(x):
    curr_workout_cals = history.find_one({"_id": CURRENT_USER_ID})['workout_cals']
    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"workout_cals" : x + curr_workout_cals}})

# takes string as last workout method
def db_update_last_workout(str_method):
    history.find_one_and_update({"_id": CURRENT_USER_ID},
        {"$set": {"last_workout" : str_method}})

########################################## OTHER ##########################################

def get_age(dob):
    dob = [int(numeric_string) for numeric_string in dob]
    today = datetime.today().strftime('%Y-%m-%d')
    today = [int(numeric_string) for numeric_string in today]
    age = today[0] - dob[0] - ((today[1], today[2]) < (dob[1], dob[2]))
    return age
'''
Example of user collection
user = {
  "username": "Test",
  "password": "pTest",
  "weight": 0,
  "height": 0,
  "activity_level": SEDENTARY,
  "diet": NO_RESTRICTIONS,
  "gender": OTHER,
  "dob": "1970-01-01"
}

'''

'''
current_user_id = ObjectId('616ce97e7225695d911646aa')
current_user_settings = db.users.find_one({'_id': current_user_id})
current_user_history = db.history.find_one_and_update(
    {'_id': current_user_id},
    {'$set': {'linked': True}},
    upsert=True,
    return_document=ReturnDocument.AFTER)
'''
# get data from HTML form
# can be replaced with separate update methods
'''
history_instance = {
    "eaten_cals": 1,
    "workout_cals": 0,
    "calorie_goal": 2000,
    "water_tracked": 500,
    "water_goal": 3000,
    "last_workout": "bike",
    "linked": False
}

history.insert_one(history_instance)
'''
# users.insert_one(user)
#users.update_one({'_id': '616cc83d32d3b6e1c7121e62'},  {"$set": user}, upsert=True)


# my_collection = db['my_collection']
# index_name = 'my_index'
# my_collection.create_index(..., name=index_name, unique=False)


# get inserted unique id
#user_id = users.insert_one(user).inserted_id

#db.list_collection_names()

# for x in users.find():
#  print(x)

# for x in mydoc:
#  print(x)

#myquery = { "height": 0 }
# users.delete_one(myquery)

#myquery = { "username": "Test" }
#newvalues = { "$set": { "username": "Test2" } }

#users.update_one(myquery, newvalues)

# print "users" after the update:
#print("db.users documents: ")
# for x in users.find():
#  print(x)

#query = {"weight": 0}
#d = users.delete_many(query)

# search
# find_one() returns a single document
'''
OPTIONAL: precede 'users' with  'pprint.pprint()'
>>>users.find_one({"username": "username", "password": "plaintext"})
>>>users.find_one({"_id": user_id})

'''
# The result is a dictionary matching the one that we inserted previously.
# NOTE: Note that an ObjectId is not the same as its string representation str(user_id)

'''
 common task in web applications is to get an ObjectId from the request URL and find the matching document. It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
'''
