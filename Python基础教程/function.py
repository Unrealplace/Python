# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

def getMaxAgeAndMinAgeFromList(ageList):
	maxAge = 0
	minAge = 0
	if isinstance(ageList,list):
		for x in ageList:
			maxAge+=x
			pass
		return maxAge,minAge
	else:
		return None



print(getMaxAgeAndMinAgeFromList([1,2,3,5,6,7,87]))
print(getMaxAgeAndMinAgeFromList('hlllll'))


#参数的默认值

def sum(a,b,c=10):
	return a+b+c
	pass

print(sum(1,2))


def listCreate(L=[]):
	L.append('helo world')
	return L
	pass

def dictCreate(D={}):
	
	pass
