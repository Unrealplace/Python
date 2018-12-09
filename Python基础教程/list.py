#list 列表类型数据结构，可以随时添加和删除其中的元素

namelist = ['liyang','yangli','oliverllee']

print('namelist = ',namelist)

print('length = ',len(namelist))

for x in range(0,len(namelist)):
	print('itme = ',namelist[x])
	pass

#list[正数] 正向取值 list[负数] 反向取值

if namelist[1] == namelist[-2]:
	print('相等噢')
	pass

#list 是个可变的列表可以增加元素
namelist.append('熊晓红大美女你好啊')

print(namelist)

#list  可以在指定位置插入元素
namelist.insert(1,'熊晓红是个大美女')

#list 删除指定位置的元素 ,如果不写索引的话默认删除最后一个元素
namelist.pop(3)

print(namelist)

#list 替换某个位置的元素
namelist[0] = 'oliver lee love xiongxiaohong'

print(namelist)