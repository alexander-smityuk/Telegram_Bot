import requests
import json

def get_rates():
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    data = json.loads(response.text)
    return data
