# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。

numSet = set([1,3,4,6,6,6])

print(numSet)

#重复元素会自动被去掉


#增加一个元素
numSet.add('hell')
numSet.add(4444)
numSet.add((1,4,6))

print(numSet)

#删除一个key
numSet.remove(4444)
numSet.remove('hell')
print(numSet)

s1 = set([1,2,3,5,6])
s2 = set([4,5,6,7,8,9])

#集合的交集 并集 操作

s3 = s1 & s2
s4 = s1 | s2

print('s3',s3)
print('s4',s4)