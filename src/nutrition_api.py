'''Fetch nutritional information for a given food item using Spoonacular API.
'''


import requests, os, json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SPOONACULAR_KEY")

def get_nutrition(food):
    url = "https://api.spoonacular.com/food/ingredients/search"
    params = {"query": food, "apiKey": API_KEY}
    res = requests.get(url, params=params)
    
    if res.status_code == 200:
        data = res.json()
        return data["results"][:1]   # return first match
    return {"error": res.text}

if __name__ == "__main__":
    food = input("Enter a food item: ")
    result = get_nutrition(food)
    print(json.dumps(result, indent=2))
