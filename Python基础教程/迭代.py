# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如Java代码：

# 可以看出，Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

from collections import Iterable

list1 = [1,2,3,4,5,6,7,8]
dict1 = {
	'name':'hello',
	'age':111,
	'title':'oooooo'
}
tuple1 = (1,33,4,5,6,7,8)
set1 = set(list1)
string = 'ABBOBGOGNOSNIOGBSOGBPNGPS'



for x in list1:
	print(x)
	pass

for x in dict1:
	print(x)
	pass

for x in tuple1:
	print(x)
	pass

for x in set1:
	print(x)
	pass
for x in string:
	print(x)
	pass

if isinstance(string,Iterable):
	for i,value in enumerate(string):
		print('index:%d,value:%s'%(i,value))
	pass

if isinstance(list1,Iterable):
	for i,value in enumerate(list1):
		print('index:%d,value:%s'%(i,value))

if isinstance(dict1,Iterable):
	for i,value in enumerate(dict1):
		print('index:%d,value:%s'%(i,dict1[value]))

