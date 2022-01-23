# 闭包函数
# 闭指的是；该函数是一个内部函数
# 包指的是：指的是该内部的函数名字在外部被引用

def outer(): # 没有调用outer()，但是创造了outer这个函数
    # 1 只检测函数体outer的语法，不执行函数体代码
    print('外面的函数正在运行')
    def inner():
        print('里面的函数正在运行')
    return inner  # 3 返回inner函数内存地址，想象成一个工厂钥匙

# 调用了outer(), 创造了inner这个函数
outer()
print(outer())
# 4 得到里面工厂的钥匙，钥匙取一个名字inner
inner=outer() # 2 定义了inner函数
# 5 里面的钥匙加括号就可以开启里面的工厂
inner()

# 为函数体传值的方式一：参数
def func(x,y):
    print(x+y)
func(1,2)

# 为函数体传值的方式二：闭包
def outer(x,y):
    def func():
        print(x + y)
    return func
func=outer(1,2)
func()

