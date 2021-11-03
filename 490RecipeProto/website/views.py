import requests
import json
from flask import Blueprint
from flask.templating import render_template


#set up blueprint 
views = Blueprint('views',__name__)

#define view
@views.route('/', methods = ['GET','POST'])
def home():
   response = requests.get("https://api.spoonacular.com/recipes/636243/information?includeNutrition=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/642178/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/664080/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data ,data2 = data2,data3 = data3)

@views.route('/', methods = ['GET','POST'])
def remove_html_tags(text):
   """Remove html tags from a string"""
   import re
   clean = re.compile('<.*?>')
   return re.sub(clean, '', text)

 
@views.route('/french/',methods=['GET','POST'])
def next1():
   response = requests.get("https://api.spoonacular.com/recipes/650239/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/648641/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/664689/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

@views.route('/japanese/',methods=['GET','POST'])
def next2():
   response = requests.get("https://api.spoonacular.com/recipes/11772/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/648500/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/660493/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

@views.route('/chinese/',methods=['GET','POST'])
def next3():
   response = requests.get("https://api.spoonacular.com/recipes/644826/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/918033/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/91894/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

@views.route('/spanish/',methods=['GET','POST'])
def next4():
   response = requests.get("https://api.spoonacular.com/recipes/660868/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/1095794/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/632706/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

@views.route('/italian/',methods=['GET','POST'])
def next5():
   response = requests.get("https://api.spoonacular.com/recipes/636910/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/642722/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/658544/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

@views.route('/european/',methods=['GET','POST'])
def next6():
   response = requests.get("https://api.spoonacular.com/recipes/715495/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response2 = requests.get("https://api.spoonacular.com/recipes/658515/information?includeInstructions=true&apiKey=f602c24d536945e6b0a9d94748614609")
   response3 = requests.get("https://api.spoonacular.com/recipes/644885/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
   data = json.loads(response.content)
   data2 = json.loads(response2.content)
   data3 = json.loads(response3.content)
   return render_template("recipeChange.html", data = data,data2 = data2, data3 =data3)

   