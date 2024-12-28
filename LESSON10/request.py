import json

import requests

web_site = 'https://jsonplaceholder.typicode.com/posts'

print('_______________GET__________________')
response = requests.get(url=web_site + '/1')
data = response.json()
print(json.dumps(data, indent=4))
print('_______________POST__________________')

