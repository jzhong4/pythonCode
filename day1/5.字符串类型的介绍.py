# 字符类型：str
# 引号可以是单引号，双引号，三引号（不怎么用）
# 三引号可以用做注释
'''dahai'''
name = '大海'
name1 = "大海2"
name2 = '''大海3'''
print(name,name1,name2)

# 字符串里面有引号
print('my name is "dahai"')
print("my name is 'dahai'")

# 字符串可以加起来
print('dahai' + 'dsb')
print('大海' * 10)

# 索引
name4 = 'abcdef'
# 取出第一个英文字符
print(name4[0])
# 倒过来取
print(name4[-1])
# 取出第一个中文字符
print(name[0])

msg = 'hello world'
print(msg[0])
print(msg[-1])

# 字符串切片（顾头不顾尾，步长），查找字符串当中的一段【起始值：终止值：步长】
print(msg[0:5])
print(msg[0:5:1])
print(msg[0:5:2])
# 了解
print(msg[::])
print(msg[0::])
print(msg[0::2])
# 步长是负数
print(msg[::-1])
print(msg[10::-1])
print(msg[10:5:-1])

# 长度len方法，可以计算长度
print(len(msg))

# 成员运算in和not in：判断一个字符串是否存在于一个大字符串中
# 返回True False
print('dahai' in 'dahai is dsb')
print('xialuo' not in 'dahai is dsb')





















