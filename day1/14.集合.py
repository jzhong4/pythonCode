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