import requests

url = 'http://httpbin.org/post'

data = {
	'name':'jack',
	'age':222
}

response = requests.post(url,data)

print(response.text)