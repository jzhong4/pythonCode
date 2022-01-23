
'''
1.描述一下对象和类的区别
2.绑定方法和非绑定方法的原理
3.定义一个Student类，有姓名，年龄，性别实例/对象属性，定义一个自我介绍的方法，可以打印出自己
的姓名，学号和年龄的信息。
'''
class Student:
    name =''
    age = 0
    sex = '男'
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def introduce(self):
        print('My name is %s, I am a %s years old %s'%(self.name,self.age,self.sex))

student1= Student('junjie', 30, 'male')
student1.introduce()