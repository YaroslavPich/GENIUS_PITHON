import json

import requests

web_site = 'https://jsonplaceholder.typicode.com/posts'
# 1
print('_______________GET__________________')
response_get = requests.get(url=web_site + "/1")
print(response_get.headers)
data = response_get.json()
print(json.dumps(data, indent=4))
# 2
print('_______________Params________________')
param = {"userId": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"}
response_get_param = requests.get(url=web_site, params=param)
print(response_get_param.text)
# 3
print('_______________POST__________________')
body = {
	"username": "Vasilij",
	"password": "123456"
}
header = {
	'Date': 'Sat, 28 Dec 2024 14:36:27 GMT',
	'Connection': 'keep-alive'
}
response_post = requests.post(url=web_site, json=body, headers=header)
print(response_post.status_code)
print(response_post.reason)
print(response_post.text)
# 4
print('_______________Query_________________')
response_query = requests.get(url=web_site + '/1')
print(f"Headers: {response_query.headers}")
print(f"Body: {response_query.text}")
# 5
print('_______________Except_________________')
try:
	response_exc = requests.get(url=web_site + "/1")
	print(response_exc.text)
except requests.exceptions.RequestException as e:
	print(f"Request exception: {e}")
# 6
print('________________Save_________________')
response_file = requests.get(url='https://jsonplaceholder.typicode.com')
with open('web_site.html', 'w', encoding='UTF-8') as file:
	file.write(response_file.text)