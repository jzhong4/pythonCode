# 装饰器就是一个特殊的闭包函数
# 什么是装饰器(就是一个函数，只不过这个函数不是给自己使用的，是个其他函数添加功能的)
#     器指的是工具，而程序中的函数就具备某一功能的工具
#     装饰指的是为被装饰器对象添加额外的功能
# 为什么要用装饰器
# 软件维护要遵循开放封闭原则
# 开放封闭原则指：
# 软件一旦上线运行后对修改源代码是封闭的，对扩展功能是开放的
# 这就用到了装饰器
# 装饰器必须遵守两大原则：
# 1.不修改被装饰对象的源代码
# 2.不修改被装饰对象的调用方式

# 违反1
# def run():
#     print('跑步')
#     print('健身')
# run()

# 违反2
# def fitness():
#     print('健身')
#     run()
# def run():
#     print('跑步')
# fitness()

# 装饰器就是在遵循1和2的原则前提下为被装饰器对象添加新功能

name = '大海'

def run(name):
    print('======')
    print('我是%s'%name)
    print('======')

def docorate(func):
    def new_func(name):
        print('我是装饰函数前面的代码')
        func(name)
        print('我是装饰函数后面的代码')
    return new_func

# 1.定义了new_func(name)函数 2.返回了new_func内存地址 3.传入了一个run函数名
run=new_func=docorate(run)
run(name)

from datetime import datetime
def run_time(func):
    def new_func(*args, **kwargs):
        start_time=datetime.now()
        print('开始时间%s'%start_time)
        func(*args, **kwargs)
        end_time=datetime.now()
        print('结束时间%s' % start_time)
        time1= end_time - start_time
        print('花费时间%s'%time1)
    return new_func

# 测试for循环从1加到9000000的时间
def for1(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    print(sum1)
for1(1)

# 1.定义了new_func(n)函数 2. 返回了new_func内存地址 3.传入了一个for1函数名
# 换个马甲
for1=new_func=run_time(for1)
for1(1)

# 测试for循环从1加到9000000的时间
@run_time  # for2=run_time(for2)
def for2(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    print(sum1)
for2(1)

# 装饰器的要求高于闭包 - 两个原则






