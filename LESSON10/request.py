import requests

web_site = 'https://jsonplaceholder.typicode.com/'

response = requests.get(url=web_site)
print(response.text)