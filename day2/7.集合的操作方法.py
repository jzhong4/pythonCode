# 集合 set
# 用途：关系运算
# 定义方式：在{}内用逗号分开多个值
# 元素不能有重复
# 集合里的元素是无序的

s = {1,2,'大海'}
print(s)
print(type(s))

s1 = {'a','b','c'}
s2 = {'a','c','d'}
print(s1 & s2) # 交集
print(s1 | s2) # 并集
print(s1 - s2) # 差集

# 补充
# 每个值都必须是不可变类型
# 错误示范
#sss={'a',1,{'name':'dahai'}}

# 增 add
s.add('小海')
# 集合是可变类型
print(s)

# 删 pop 看你的pycharm是怎么无序排列的，从第一个元素删除
s.pop()
print(s)

# 指定删除remove
s.remove('大海')
print(s)

# 改
# update
s.update(['蓝海','紫海'])
print(s)

s1=list(s)
s1[0]=8
s=set(s1)
print(type(s))
print(s)

# 集合去重
# 局限性
# 无法保证原数据类型的顺序
# 数据里要保证是不可变类型时才能用集合去重
names = ['dahai','xialuo','xishi','dahai','dahai','dahai']
s=set(names)
print(s)
l=list(s)
print(l)

# 要用for循环和if判断去重就可以保证顺序和对可变类型的去重
# 总结
# 字符串，数字，布尔都是一个值，改变需要重新赋值，都是不可变类型
# 容器元组是不可变类型，字典，列表，集合都是可变类型


