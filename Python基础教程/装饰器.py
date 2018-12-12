
import time

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
		pass
	return wrapper
	pass

@log
def nowTime():
	print('22.22.22.22')
ftime = nowTime
ftime()

#函数对象有一个__name__属性，可以拿到函数的名字：
print(ftime.__name__)


print('xxxxxxx')
print(nowTime())


#装饰器模式用法，不带参数
def sleep(func):
	def wrapper():
		func()
		print('start sleeping')
		pass
	return wrapper
	pass

@sleep
def eat():
	print('start eating')

eat()

#装饰器模式用法，带参数
def decorator1(func):
	def wrapper(name):
		start = time.time()
		print(start)
		func(name)
		endtime = time.time() - start
		print(endtime)
		pass
	return wrapper
	pass

@decorator1
def decorator1func(name):
	for x in range(1,10000000):
		pass
	print(name)
	pass

decorator1func('ooooooooo')




