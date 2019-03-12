import requests

url = 'http://httpbin.org/get'

data = {
	'name':'zhangsan',
	'age':33
}

response = requests.get(url,data)

#请求地址
print(response.url)
print('####################\n')
#字符串数据
print(response.text)
print('####################\n')
#响应头
print(response.headers)
print('####################\n')
#请求头
print(response.request.headers)
#打印json数据
print('####################\n')
print(response.json())

