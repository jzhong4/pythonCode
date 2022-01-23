# 大前提：生成器就是一种自定义的迭代器，本质就是迭代器
# 但凡函数内包含yield关键字，调用函数不会执行函数体代码，
# 会得到一个返回值，该返回值就是生成器对象
def func():
    print('=====1')
    yield 1
    print('=====2')
    yield 2
    print('=====3')
    yield 3
g=func()
# print(g)
# print(g is g.__iter__().__iter__())
#g.__next__()
# res1=next(g)
# 会触发函数的执行，直到碰到一个yield停下来，并且将yield后的值当做本次next的结果返回
# print(res1)
#
# res2=next(g)
# print(res2)
# res3=next(g)
# print(res3)
# 报错和迭代器一样，代表取完了
# next(g)
for i in g:
    print(i)

# 总结yield：只能在函数内使用
# 1.yield提供了一种自定义迭代器的解决方案
# 2.yield可以保存函数的暂停状态
# 3.yield对比return
  # 1.相同点：都可以返回值，值的类型与个数都没有限制
  # 2.不同点：yield可以返回多次值，而return只能返回一次函数值就结束了

'''
定义一个生成器，这个生成器可以生成10位斐波那契数列，得到斐波那契数列
# 斐波那契数列，数列中每一个数的值都等于前两个数相加的值 1,1,2,3,5,8,13,21,34,55
'''