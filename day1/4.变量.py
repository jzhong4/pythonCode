# 定义变量的语法
name = '大海'
print(name)
name = '小红'
print(name)

# 变量命名规则
# 第一个字符不能是数字
# 字母，数字，下划线任意组合（区分大小写）
age_of_dahai = 18
# 驼峰体
AgeOfDahai = 18
# 常量 - 全部是大写，告诉别人不能改，虽然可以改
NAME = '小海'
# 变量的特性
# id相当于内存中的位置或者地址
print(id(name))
print(id(NAME))
