import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
def get_loc():
    response = urlopen(url)
    data = json.load(response)

    return data['loc']



