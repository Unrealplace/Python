import requests

url = 'http://132.232.194.21/hello.html'

respons = requests.get(url)

print(respons.text)