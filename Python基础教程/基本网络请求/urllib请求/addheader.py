from urllib import request,parse
url = "http://httpbin.org/post"
headers = {
#伪装一个火狐浏览器
"User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
"host":'httpbin.org'
}
dict = {
"name":"Germey"
}
data = bytes(parse.urlencode(dict),encoding="utf8")
req=request.Request(url=url,data=data,headers=headers,method="POST")# 利用更强大的 Request 类来构建一个请求
response = request.urlopen(req)
print(response.read().decode("utf-8")) 

# 也可以通过更加灵活的方式添加headers 如:
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

