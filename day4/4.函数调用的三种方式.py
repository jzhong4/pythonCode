# 1.语句形式
#def foo():
#    print('from foo')
#foo()

# 表达式形式
def foo(x, y):
    res = x + y
    return res
res = foo(1,2)
print(res)
res1 = foo(1,2) * 100
print(res1)

# 可以当成参数传给另一个函数
def max2(x,y):
    if x > y:
        return x
    else:
        return y
print(max2(1,2))
print(max2(max2(1,2),max2(4,5)))



