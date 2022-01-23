'''
1. 什么是封装
   装:往容器/名称空间里存入名字
   封：代表将存放于名称空间中的名字藏起来，这种藏对外不对内
2. 为何要封装
   封数据属性：？？？
   封函数属性：？？？
3. 如何封装
   在类内定义的属性前加__开头(注意是2杠)
'''

class Foo:
    __x = 11
    __y = 22
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __func(self):
        print('func')
    # 接口
    def get_info(self):
        print(self.__x,self.__y,self.name)
        self.__func()

#print(Foo.__x)
# 1. __开头的属性到底如何实现的隐藏
print(Foo.__dict__)
# _类__属性名

## __开头的属性实现的隐藏仅仅只是一种语法意义上的变形，并不会真的限制外部的访问
## 我们不会这么做
#print(Foo._Foo__x)

# 误区封装是定义类阶段进行的
# 该变形操作只在类定义阶段检测语法时发生一次，类定义阶段之后新增的__开头的属性
# 并不会变形
# Foo.__z=333
# print(Foo.__z)
# print(Foo.__dict__)

# 2.如何实现的对外隐藏，对内不隐藏
obj=Foo('大海',18)
#obj.__func()
obj.get_info()

class Foo:
    def __f1(self):  # _Foo.__f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        # obj.f1()是Bar()对象
        self.__f1() # _Foo__f1
        # self.__f1() self._Foo__f1() 类定义的时候进行了统一

class Bar(Foo):
    def __f1(self):  # _Bar__f1
        print('Bar.f1')

obj=Bar()
obj.f2()

'''
Foo.f2
Foo.f1
'''

