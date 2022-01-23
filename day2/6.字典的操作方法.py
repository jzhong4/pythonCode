# 字典类型：dict
# {}内，逗号隔开多个key：value元素，其中value可以是任意数据类型，key通常是字符串类型

info = {'name':'大海','age':18}
print(info['name'])
print(info['age'])
print(info)

# 列表和字典的区别
# 列表依靠索引
# 字典依靠键值对 # key描述性的信息

# 生成字典的方式2
dic = dict(x=1, y=2)
print(dic)

# 字典的增加操作
print(info)
# 直接赋值一个不存在的key和value
info['addr'] = 'changsha'
print(info)

# 字典添加的时候也要没有进行重新赋值，所以字典是不可变类型

# 字典len查看的是键值对的个数
print(len(info))

# 成员运算in 和 not in：字典的成员运算判断的是key 返回的是布尔类型
print('name' in info)
print('大海' in info)

#删
#clear 清空字典
#info.clear()
#print(info)

#del
#del info['name']
#print(info)
#不存在的key会报错
#del info['XXX']

# pop删除 返回value，实际上就是拿走了字典的value
#res=info.pop('addr')
#print(info)
#print(res)

# popitem 最后一个键值对删除，字典无序，返回的是一个元组
#res1 = info.popitem()
#print(res1)
#print(info)

# 改
info['name']='红海'
print(info)
info.update({'name':'xiaohai'})
print(info)
# setdefault
# 有则不动/返回原值，无则添加/返回新值
res=info.setdefault('name','xxx')
print(info)
print(res)

res2=info.setdefault('sex','male')
print(info)
print(res2)

# 查
print(info['name'])
# 查一个不存在的key会报错
# print(info['XXX'])

print(info.get('name'))
# 没有key就返回None，不会报错
print(info.get('XXX'))

# 取出所有的key
print(list(info.keys()))

# 取出所有的值
print(list(info.values()))

# 取出所有的键值对
print(list(info.items()))
