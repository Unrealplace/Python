a = 100

if a > 10:
	print('a>10')
else:
	print('a<=10')
	pass

# 布尔值
# 布尔值可以进行 and or not 运算 对应的是 && || ！

b = 44
c = 444
d = True
e = False

if b > c:
	a = b + c

	pass

if  d and e:
	print(a)
	pass

if d or e:
	print(b)
	pass

if not e:
	print(c)
	pass

# 空值 None

f = None
print(f)

# 常量 用大写的变量名表示 常量 PI = 3.14159265359

#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
#所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。

BASEURL = 'http://www.baidu.com'
BASEURL = 'htttttt'

print(BASEURL)
