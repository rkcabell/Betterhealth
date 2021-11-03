import requests


def calorie_calc(Ingredient_unformatted):
    #Ingredient_unformatted = "1 cup sugar"
    _ingr = Ingredient_unformatted.replace(" ", "%20")
    response = requests.get('https://api.edamam.com/api/nutrition-data?app_id=fdb7ea11&app_key=09001dad57a62484bd663dab44500239&nutrition-type=cooking&ingr=' + _ingr)
    data = response.json()
    if data['calories'] == 0:
        return("Invalid Entry: Check spelling and format")
        #print("Don't forget to include ingredient amount")
    else:
            # display calories to web page
            # print("Calories: ")
            return  (data['calories'])
            # save unformatted ingr to db
            # print("String to save to db: ")
            # print(Ingredient_unformatted)