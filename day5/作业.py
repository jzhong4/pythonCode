'''
写一个登陆装饰器对以下函数进行装饰，要求输入账号和密码才能运行该函数
def run():
    print(‘开始执行函数’)
'''
def run():
    print('开始执行函数')

def decorate(func):
    def new_func():
        account=input('输入账号')
        password=input('输入密码')
        func()
    return new_func
decorate(run)()