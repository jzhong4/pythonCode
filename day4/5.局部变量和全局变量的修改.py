# 1.外部不能访问函数内部的变量
def fun1():
    x=1
#print(x)

# 函数内部能够访问函数外部的变量
x = 123
def fun2():
    print(x)
fun2()

# 函数不能修改函数外面的变量
# 错误示范
#x = 123
#def fun3():
#    x = x + 1
#    print(x)
#fun3()

# global 能让我们在函数里面去修改全局变量的值
x = 123
def fun3():
    global x
    x = x + 1
    print(x)
fun3()

# nonlocal 让嵌套函数能够修改嵌套函数之外的值
def func2():
    b = 100
    def func3():
        print('=====')
        nonlocal b
        b += 1
        print(b)
    func3()
func2()





