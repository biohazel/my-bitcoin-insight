import requests

def get_current_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    data = requests.get(url).json()
    return float(data["bpi"]["USD"]["rate_float"])

