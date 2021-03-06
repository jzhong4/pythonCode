'''
匿名函数：就是没有名字的函数
为何要用：用于仅仅临时使用一次的场景，没有重复使用的需求
'''

# 匿名函数，除了没有名字其他都有
# 语法：lamda空格+参数+冒号+函数体代码(表达式或者函数)
# 一行代码图省事
# 匿名函数定义
print(lambda x, y: x + y)
# 调用直接内存地址加括号 + 括号可以调用
# 返回值省去了return
# 表达式
print((lambda x, y: x + y)(1,2))
# 函数
(lambda x, y: print(x + y))(1,2)

# 匿名函数与内置函数结合使用
# max, min, sorted
salaries = {
    'xiaoluo':3000000,
    'xishi':10000,
    'dahai':3000
}
# 求薪资最高的那个人民：即比较的是value，但取结果是key
# 默认比较key的值
print(max(salaries))
# max(字典，key=函数名)
def func(name):
    return salaries[name]
print(max(salaries,key=func))
print(max(salaries,key=(lambda name: salaries[name])))

# 求最小值
print(min(salaries,key=(lambda name: salaries[name])))

nums=[11,33,22,9,1]
res=sorted(nums,reverse=True)
print(res)

# 循环遍历薪资
for v in salaries.values():
    print(v)
# 薪资反序
print(sorted(salaries, key=(lambda name:salaries[name]),reverse=True))







