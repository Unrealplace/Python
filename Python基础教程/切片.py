
#list 切片
L = ['helloworld','liyang','bob','peter','cat','job']

newList = []

for x in range(0,len(L)):
    if x < 3:
    	newList.append(L[x])

print(newList)

newList = L[:3]

print(newList)

newList = L[1:]

print(newList)

newList = L[-2:]

print(newList)

#每隔 2 个 取一次
newList = L[:10:2]
print(newList)
#每隔 3 个取一次
newList = L[::3]

print(newList)


# 字符串的切片操作

name = 'hellworld--nice to meet you'
key = name[:6]
print(key)


# tuple 切片

namTuple = (1,2,3,3,4,6,6,7,8,88,8,8,)
key = namTuple[:10:2]
print(key)
