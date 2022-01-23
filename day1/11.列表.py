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
