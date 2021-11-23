import requests


def calorie_calc(Ingredient_unformatted):
    #Ingredient_unformatted = "1 cup sugar"
    _ingr = Ingredient_unformatted.replace(" ", "%20")
    response = requests.get('https://api.edamam.com/api/nutrition-data?app_id=fdb7ea11&app_key=09001dad57a62484bd663dab44500239&nutrition-type=cooking&ingr=' + _ingr)
    data = response.json()
    if data['calories'] == 0:
        return("Invalid Entry: Check spelling and format")
    elif _ingr[0] == '-':
        return("Invalid Entry: Check spelling and format")
    else:
            return  (data['calories'])
