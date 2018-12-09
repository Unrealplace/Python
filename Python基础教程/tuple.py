# 另一种有序列表叫元组：tuple。\
# tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
nametuple = ('oliverlee','liyang','yanglie')

# 定义一个空的tuple
emptytuple = ()

# 定义一个值的tuple,要用，隔开

onetuple = (1,)

print('nametuple = ',nametuple)
print('emptytuple = ',emptytuple)
print('onetuple = ',onetuple)

nametuple[1] = 'niec to meett you'

print(nametuple)