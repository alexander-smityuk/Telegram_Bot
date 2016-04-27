import requests
import json


def get_rates(ccy):
    # API url
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    # Get request for API
    response = requests.get(url)
    # Parse JSON data
    data = json.loads(response.text)
    result = ''
    # Search for ccy
    for item in data:
        if item['ccy'] == ccy:
            result = 'Валюта: ' + item['ccy'] + "\n" \
                     + 'Покупка: ' + str(round(float(item['buy']), 2)) + " грн" + "\n" \
                     + 'Продажа: ' + str(round(float(item['sale']), 2)) + " грн" + "\n"
            break
    return result
