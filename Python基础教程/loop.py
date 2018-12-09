# 循环的使用

namelist = ['fanyangyang','yangyangfan','oliverlee']
nametuple = ('hello','world','nice ','to','meet you')

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

for name in namelist:
	print(name)
	pass

for item in nametuple:
	print(item)
	pass

#遍历索引的方式
for x in range(1,10):
	print(x)
	pass