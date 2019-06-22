#Dependencies and Set up
import requests
import json


url = ('https://www.alphavantage.co/query?function=SECTOR&apikey=DIH7DPEEI0O1P4FW')

response = requests.get(url)

data = response.text
parsed = json.loads(data)

print (data)