
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name , age , gender = 'boy'):
		super(Dog, self).__init__()
		self.name = name
		self.age  = age
		#设置属性权限控制
		# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
		self.__gender = gender

	def get_name():
		return self.name
		pass
	def get_gender():
		return self.__gender
		pass
	#这里修改要传入self 对象
	def set_gender(self,gender):
		self.__gender = gender
	def description(self):
		print('%s,%s,%s'% (self.name,self.age,self.__gender))
	def run():
		print('我是父类的run')
		pass



dog = Dog('dogggg',111)
dog.description()
dog.name = 'llllll'
dog.age = 34333
# dog.__gender = 'girl'
dog.description()
dog.set_gender('girl')
dog.description()


class Cat(Dog):
	"""docstring for Cat"""
	def __init__(self):
		

	def run():
		super.run()
		print('我是子类的run')
		pass


cat = Cat()
cat.run()
		



		