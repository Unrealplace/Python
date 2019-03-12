import urllib.parse
import urllib.request

urlStr = 'http://httpbin.org/post'

#  urllib.parse.urlencode() 方法来将参数字典转化为字符串
data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')

# 传参: data 参数是可选的，如果要添加 data ，
# 它要是字节流编码格式的内容，即 bytes 类型，通过 bytes() 函数可以进行转化，
# 另外如果你传递了这个 data 参数，它的请求方式就不再是 GET 方式请求，而是 POST

response = urllib.request.urlopen(urlStr,data=data)

print(response.read())