#匿名函数

# 使用兰姆达表达式

funcList = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))

print(funcList)

def func(x,y):
	return lambda:x * x + y * y
	pass
backFunc = func(111,222)


print(backFunc())