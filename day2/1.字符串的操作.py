# 字符串方法
# 字符串拼接
# 增
print('dahai' + 'dsb')

# format
print('my name is {}'.format('dahai'))
# 可以通过索引
print('my name is {1} my age is {0}'.format(18,'dahai'))
#  可以通过关键字
print('my name is {name} my age is {age}'.format(age=18,name='dahai'))

# join - 列表转字符串
str1 = '真正的勇士'
str2 = '敢于直面惨淡的人生'
str3 = '敢于正视淋漓的鲜血'
print(''.join([str1, str2, str3]))
print('，'.join([str1, str2, str3]))
print('哇塞'.join([str1, str2, str3]))
# 空格也属于字符
print(' '.join([str1, str2, str3]))

# 删
name1 = 'dahai'
del name1
#print(name1) -- name1 没有了

# 改
# 字符串字母变大写和变小写 lower,upper
msg1 = 'abc'
msg2 = msg1.upper()
# 原值
print(msg1)
print(id(msg1))
# 修改后的值，需要重新赋值，原值不改变
print(msg2)
print(id(msg2))

# 把第一个字母转化成大写 capitalize
letter = 'abcd'
print(letter.capitalize())
# 每个单词的首字母进行大写转换 title
letter_msg = 'hello world'
print(letter_msg.title())

# 把字符串切分成列表，split 默认空格字符切分
msgg = 'hello world python'
# 默认以空格切分
print(msgg.split())
# 可以切分你想要的字符 比如 *
msgg1 = 'hello*world*python'
print(msgg1.split('*'))
# 切分作用，split后可以取值
msggg = 'root:123456'
print(msggg[0:4])
print(msggg.split(':')[0])
print(msggg.split(':')[1])

# 去掉字符串[左右]两边的字符strip，不写默认是空格字符,不管中间的其他字符
user = '    da hai   '
print(user)
print(user.strip())
#name = input('请输入用户名').strip()
#print(name)

# 了解
# center，ljust,rjust, 多余添加自己想要的字符
print('dahai'.center(11,'*')) # ***dahai***
print('dahai'.ljust(11,'*'))  # dahai******

# 查
# find，index
# 查找子字符串在大字符串的哪个位置 (起始索引)
msga = 'hello dahai is dsb'
print(msga.find('dahai'))
# 没找到会返回-1
print(msga.find('ddddd'))
print(msga.index('dahai'))
# 没找到会报错
#print(msga.index('ddddd'))

# 统计一个子字符串在大字符串中出现的次数 count
msgb = 'hello dahai is dsb dahai'
print(msgb.count('dahai'))

# 判断一个字符串里的数据是不是都是数字 isdigit #返回布尔值
num = '1818'
num1 = '18aaa18'
aaa = 'aaa'
print(num.isdigit())
print(num1.isdigit())

# 判断一个字符串里的数据是不是都是字母 isalpha #返回布尔值
print(aaa.isalpha())
print(num.isalpha())
print(num1.isalpha())

# 比较开头的元素是否相同 startswith
# 比较结尾的元素是否相同 endswith
# 返回布尔值
mm = 'dahai xialuo'
print(mm.startswith('dahai'))
print(mm.endswith('xialuo'))

# 判断字符串中值是否全是小写的 islower
# 判断字符串中值是否全是大写的 isupper
letter2 = 'ABC'
letter3 = 'abc'
print(letter2.isupper())
print(letter3.isupper())
print(letter2.islower())
print(letter3.islower())

# 字符串的转义
# 加了 \ 字符不再表示它本身的含义
# 常用 \n \t
# \n 换行符
print('hello \n python')
# \t 横向换行符，相当于一个tab
print('hello \t python')

print(r'hello \t python \n') # 一次性搞定
print('hello \\t python \\n')

