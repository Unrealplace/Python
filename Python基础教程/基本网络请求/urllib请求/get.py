from urllib import request

url = 'http://www.baidu.com'
response = request.urlopen(url)

print(response.read().decode('utf-8'))


# Urllib是python内置的HTTP请求库
# response 响应可调用 read() 、readinto() 、getheader(name) 、 getheaders() 、 fileno() 等函数
# 和 msg 、 version 、 status 、reason 、debuglevel 、 closed 等属性

