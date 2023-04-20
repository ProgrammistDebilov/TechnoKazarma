import json
import time
from urllib.request import urlopen
from datetime import datetime
url = 'http://ipinfo.io/json'
def get_loc():
    response = urlopen(url)
    data = json.load(response)

    return data['loc'].split(',')

if __name__ == '__main__':
    print(get_loc())
    j = datetime.now()
    print(j)
    time.sleep(10)
    print(datetime.now())
    print(datetime.now() - j)

