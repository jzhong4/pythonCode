'''
# 子类重用父类功能  *****
# 在子类派生出的新方法中重用父类功能的方式一：
# 指明道姓地引用某一个类中的函数
# 1.与继承无关
# 2.访问时类的函数，没有自动传值的效果
'''


class People:
    school='图灵学院'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Student(People):
    def __init__(self,name,age,sex,score=0):
        # 相当于调用了父类的方法
        # 指明道姓People
        People.__init__(self,name,age,sex)
        self.score = score

    def play(self):
        print('%s play football'%self.name)

class Teacher(People):
    def __init__(self, name, age, sex, hobby):
        # 相当于调用了父类的方法
        # 指明道姓People
        People.__init__(self, name, age, sex)
        self.hobby = hobby
    def course(self):
        print('%s course'%self.name)

s1 = Student('zhouyang',38,'male')
print(s1.__dict__)
t1 = Teacher('dahai',18,'male','song')
print(t1.__dict__)