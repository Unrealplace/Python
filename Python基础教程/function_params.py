
# 默认参数问题

def power(x,n=2):
	sum = 0
	while n>0:
		sum+=(x*x)
		n-=1
		pass
	return sum
	pass

print(power(10))
print(power(10,6))


def enroll(name,gender,age=12,city='BeiJing'):
	print('name = %s,gender=%s,age = %d,ciyt=%s' % (name,gender,age,city))
	pass

enroll('liyang','boy')
enroll('oliverlee','girl',1111,111)


def add_end(L=[]):
	L.append('end')
	return L
	pass

print(add_end())
print(add_end())
print(add_end())
print(add_end())

# 打印结果如下，为啥会导致这种原因呢
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# ['end']
# ['end', 'end']
# ['end', 'end', 'end']
# ['end', 'end', 'end', 'end']

def add_newAdd(L=None):
	if L is None:
		L = []
	L.append('hello')
	return L
	pass

print(add_newAdd())
print(add_newAdd())
print(add_newAdd())


# 可变参数 ,传入的参数会被组装成一个tuple

def calc(*nums):
	sum = 0
	for n in nums:
		sum+=n
	return sum
	pass

numbers = [1,2,3,5,6,6,7,7,7,7,7]

print(calc(*numbers))

def length_changeParams(*params):
	for x in range(0,len(params)):
 			print('----->',params[x])
	pass

length_changeParams(1,46,77,'lfagaga',('ggg',88,66))


# 关键字参数 会把传入的参数包装成字典
def keyWordFunc(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
	pass

keyWordFunc('liyang',11,girlFriend='xiongxiaohong')

keyWordFunc('jjj',44,aaa="fodnaga",bbb='foandgagfaga',ccc="99919191")


#命名关键字参数

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 这种方式定义的函数如下：
# def person(name, age, *, city, job):
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def nameKeyWords(name,age,*,city,job):
	print(name,city)
	pass

nameKeyWords('liyang',43,city='BeiJing',job='ios')



#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,age,*args,city,job):
	print(name,age,args,city,job)
	pass

person('李阳',27,'love',' you',' hello',' world',city='BeiJing',job='ios')

#命名关键字设置默认值操作
def person2(name,age,*,city='BeiJing',job):
	print(name,age,city,job)
	pass

person2('liyang',44444,job='andriod')

# 参数组合

# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def parass(a,b,c=0,*args,city='BeiJing',job,**kw):
	print(a,b,c,args,city,job,kw)
	pass

parass(10,11,666,999,777,888,job='ios progremer',aaa ='hello world',bbb ='llllllll')
