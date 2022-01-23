'''
反射：通过字符串来反射/映射到对象/类的属性上 *****
'''

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print('%s is running'%self.name)

obj=People('dahai',18)
print(obj.__dict__)
print(obj.name)
# obj.__dict__本质上就是在这个对象的字典里面找这个['name']

# 让用户使用属性
attr = input('用户输入属性').strip()
print(type(attr))
# 所以用户输入的是一个字符串的形式，我们怎样把它变成属性名，就用到了反射

# 判断对象是否有属性，有就返回True，没有就算False
print(hasattr(obj,'name'))
print(hasattr(obj,'aa'))

# 获取对象属性
print(getattr(obj,'name'))
print(getattr(obj,'xxx',None))
# 第三个参数找不到就返回None

#修改对象属性
setattr(obj,'name','dahai1')
print(getattr(obj,'name'))
# 不存在的直接添加
setattr(obj,'yyy',1111)
print(obj.__dict__)

#删除对象属性值
delattr(obj,'name')
print(obj.__dict__)

#print(hasattr(对象,'对象的属性'))
# 类也可以说是对象
#print(hasattr(类,'类的属性/或者方法'))
print(hasattr(list,'append'))
print(hasattr(list,'xxxx'))

# 反射方法的应用
class ShoppingCart:
    def shopping(self):
        print('shopping')
    def login(self):
        print('login')
    def football(self):
        print('football')
    def run(self):
        cmd=input('请输入>>>').strip()
        # if cmd=='login':
        #     self.login()
        # elif cmd=='shopping':
        #     self.shopping()
        # 反射方法的作用
        if hasattr(self,cmd):
            #拿到内存地址
            method=getattr(self,cmd)
            print(method)
            #调用s对象的方法
            method()
s=ShoppingCart()
s.run()



