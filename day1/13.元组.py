# 元组 tuple
# 用途：记录多个值，当多个值没有改的需求，此时用元组更合适
# 定义方式：在()内用逗号分隔开多个任意类型的值
t = (1, 2, '大海', (2, 3), [1, 2, 3])
print(t)
print(type(t))
print(t[0])
#t[0] = 5 改动有问题
#t[5] = 2
print(t[4][0]) #取值没有问题
