# 列表类型：list
# 定义：在[]内用逗号分隔开多个任意类型的值
L = ['大海', 1, 1.2, [1.22, '小海']]
print(L)

## 索引从0开始
print(L[0])
print(L[1])
print(L[-1])
print(L[3])
print(L[3][1])

xiaohai_list=L[3]
print(xiaohai_list)
print(xiaohai_list[1])

L[0] = '红海'
print(L)

# 切片（顾头不顾尾），[起始值：终止值：步长]
print(L[0:3])
print(L[0:3:1])
print(L[0:3:2])

# len长度，列表的元素
print(len(L))

# 成员运算 in 和 not in
print('红海' in L)
print('红海' not in L)

# 查看列表某个元素的个数count
print(L.count('红海'))

# 在列表中从左到右查找指定元素，找到了放回该值的下标/索引
print(L.index('红海'))
#print(L.index('海'))

# 增
# append(元素)，往列表末尾追加一个元素
L.append('蓝海')
print(L)

# 规律列表的修改和增加都不需要重新赋值，直接改变了原值，所以是可变类型
# 字符串，数字，布尔都是一个值，改变需要重新赋值，都是不可改变类型
L.append('蓝海')
print(L)

# extend() 往列表当中添加多个元素，括号里放列表，也是末尾追加
L.extend(['蓝海','紫海'])
print(L)

# insert(索引，元素) 往索引位置前插入一个元素
L.insert(1, '黄海')
print(L)

# 删除
#del L[0]
#print(L)
# 指定删除一个，从左往右
#L.remove('紫海')
#print(L)
# pop 从列表中拿走一个值, 按照索引删除值，默认删除最后一个
#L.pop()
#print(L)
# 返回值
#res = L.pop(0)
#print(res)
#print(L)
# 清空列表clear,不是把列表删掉
#L.clear()

#改
#L[0] = '白海'
#print(L)

#反序
#L.reverse()
#print(L)

# sort排序对数字
list_num = [1,3,2,5]
# 不写默认是正序
# reverse=True参数是倒序
list_num.sort(reverse=True)
print(list_num)
list_num.sort(reverse=False)
print(list_num)