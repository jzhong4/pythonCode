# 返回值是一个函数的处理结果return
'''
注意：
   1. return是一个函数结束的标志，函数可以有多个return
      但是只要执行一次，整个函数就会结束运行，默认return None
   2. return返回值无类型限制，即可以是任意数据类型
   3. return的返回值无个数限制，可以用逗号分隔开多个任意类型的值
      0个：返回None，ps：不写return默认会在函数最后一行添加return None
      1个：返回的值就是该值本身
      多个：返回值是元组
   4. return关键字：return是函数结束的标志
   那么利用这一点就可以结束循环
'''
def factory(a):
    print(a)
    c = a + 1
    print(c)
    if a == 1:
        return [1,2,3], True, 'aaa'
    return c
    #return True
    #return [1,2,3]
    # 后面都没有
    print('制造电脑')
    return 2
a=factory(1)
print(a)

# return关键字：return是函数结束的标志, 利用这点可以结束循环
def factory(a):
    print('=====')
    print('=====')
    print('=====')
    while True:
        while True:
            while True:
                if a == 3:
                    return
                a += 1;
                print(a)
factory(1)
