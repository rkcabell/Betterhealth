import requests
import json
#from json.decoder import JSONDecodeError

#gets summary from ID
#userTest = input("Please enter a food id\n")
#if not userTest:
 #userTest = input("Invalid Entry: please enter a food id\n")
#get api response
#else:
 #response = requests.get("https://api.spoonacular.com/recipes/"+userTest+"/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
# ids  American(636243,642178,664080) french(650239,648641,664689) japanese(11772,648500,660493) chinese(644826,918033,91894) spanish(660868,1095794,632706) italian(636910,642722,658544) european(715495,658515,644885)
#print(data['instructions']) 
#print(data['title'])

#American
response = requests.get("https://api.spoonacular.com/recipes/636243/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
data = response.json()
#print(data['title'])
print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/642178/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/664080/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#French
#response = requests.get("https://api.spoonacular.com/recipes/650239/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/648641/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/664689/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#japanese
#response = requests.get("https://api.spoonacular.com/recipes/11772/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/648500/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/660493/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()


#chinese
#response = requests.get("https://api.spoonacular.com/recipes/644826/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/918033/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/91894/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#spanish
#response = requests.get("https://api.spoonacular.com/recipes/660868/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/1095794/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/632706/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#italian
#response = requests.get("https://api.spoonacular.com/recipes/636910/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/642722/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/658544/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#european
#response = requests.get("https://api.spoonacular.com/recipes/715495/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/658515/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()

#response = requests.get("https://api.spoonacular.com/recipes/644885/information?includeInstructions=false&apiKey=f602c24d536945e6b0a9d94748614609")
#data = response.json()
#print(data['title'])
#print(data['image'])
#print(data['instructions'])
#print()