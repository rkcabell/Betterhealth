#https://pymongo.readthedocs.io/en/stable/tutorial.html
# see link for 
# bulk inserts, bulk querying, count num of documents,
# advanced queries, indexing(ascending)
#========================
#This file was made using a pymongo tutorial
#========================
import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId


#For default host, port
client = MongoClient()
print ("client:", client)

# For custom host, port
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

# get database
db = client.bhealth

# get a collection
# collection is roughly the equivalent to a table in a relational database
users = db.users

# Data in MongoDB is stored using JSON-style "documents"
# In PyMongo dictionaries to represent docs

# Inserting a document
# db_collection.insert_one() 
#   returns an instance of InsertOneResult(inserted_id, acknowledged)
user = {"first": "george",
        "last": "smith",
        "height": 490,
        "weight": 9001}

#get inserted unique id
user_id = users.insert_one(user).inserted_id

db.list_collection_names()

#for x in users.find():
#  print(x)

myquery = { "height": 490 }
mydoc = users.find(myquery)
#for x in mydoc:
#  print(x)

#myquery = { "height": 490 }
#users.delete_one(myquery)

myquery = { "first": "george" }
newvalues = { "$set": { "first": "chris" } }

users.update_one(myquery, newvalues)

#print "users" after the update:
print("db.users documents: ")
for x in users.find():
  print(x)
  
query = {"weight": 9001}
d = users.delete_many(query)

# search
# find_one() returns a single document
'''
OPTIONAL: precede 'users' with  'pprint.pprint()'
>>>users.find_one({"username": "Shivaz", "password": "plaintext"})
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



