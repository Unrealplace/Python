
from functools import reduce

def f(x):
	return x * x
	pass

r = map(f,[1,2,3,4,5,6,7,8,9])

#传入的第一个参数是f，即函数对象本身。
#由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

print(r)
r = list(r)
print(r)
for x in r:
	print(x)
	pass

#全部转化成字符串
print(list(map(str,[1,2,3,4,5])))
print('fffffff')


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
def add(x,y):
	return x+y
	pass

print(reduce(add,[1,3,5,7,9]))


def fn(x,y):
	return x*10 + y
	pass

print(reduce(fn,[1,3,5,7,9]))


#用 map 和 reduce 实现一个 字符串转换成数字

def char2num(s):
	digits = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9
	}
	return digits[s]
	pass

num = reduce(fn,map(char2num,'123578899'))

print(num)



