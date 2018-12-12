#函数作为返回值

def cal_sum(*agrs):
	def sum():
		ax = 0
		for x in agrs:
			ax += x
		return ax
	return sum
	pass

sum_func = cal_sum(1,2,3,4,5,6,7,8)

print(sum_func())


#闭包
def count():
	def f(j):
		def g():
			return j*j
			pass
		return g
		pass
	fs = []
	for x in range(1,4):
		fs.append(f(x))
	return fs

f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())
