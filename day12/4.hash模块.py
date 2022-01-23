# 1.什么叫hash:hash是一种算法，该算法接受传入的内容，经过运算得到一串hash值
# 2.hash值的特点是：
# 2.1 只要传入的内容一样，得到的hash值必然一样 ====》 文件完整性校验
# 2.2 不能由hash值返解成内容 ====》 把密码做成hash值，不应该在网络传输明文密码
# 2.3 只要使用的hash算法不变，无论校验内容有多大，得到的hash值长度是固定的，这样不影响传输

import hashlib
# 1.创建hash工厂
m=hashlib.md5()
# 运输的是二进制
# 2.在内存里面运送
# m.update('helloworld'.encode('utf-8'))
# 一点一点的给，因为可能二进制会很长，这个要好一些
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))

# 3.产出hash值
print(m.hexdigest())
# fc5e038d38a57032085441e7fe7010b0

# m=hashlib.md5()
# with open(r'D:\python\abc.png','rb') as f:
#     for line in f:
#         m.update(line)
#     hv=m.hexdigest()
# print(hv)
# 输入密码的时候是沿着网络传输到别的服务器上面，黑客可以把包抓下来
# 所以发给服务器端是hash值，也就是密文
# 但是还是可以抓下来
# 常用密码字典
# 什么生日，123，身份证等等 密码有强烈的个人习惯
# 那么我用一样的hash算法，是不是可以得到一样的hash值密文，那么明文肯定是一样的
# 撞库风险

# 密码前后加盐
# pwd='abc123'
# m=hashlib.md5()
# m.update('大海老师'.encode('utf-8'))
# m.update('pwd'.encode('utf-8'))
# m.update('夏洛特烦恼'.encode('utf-8'))

print(m.hexdigest())
# 黑客破译成本远大于收益成本
# 中间加盐
# pwd='abc123'
# print(pwd[0])
# print(pwd[1:])
# m=hashlib.md5()
# m.update('大海老师大帅比'.encode('utf-8'))
# m.update(pwd[0].encode('utf-8'))
# m.update('夏洛特'.encode('utf-8'))
# m.update(pwd[1:].encode('utf-8'))
# m.update('烦恼'.encode('utf-8'))
# print(m.hexdigest())

# 2.3 只要使用的hash算法不变，无论校验内容有多大，得到的hash值长度是固定的，这样不影响传输
# m=hashlib.md5()
# 运输的是二进制
# 2.在内存里面运送
# m.update('helloworldaaaaaaaaaaaaaaaaaaaa'.encode('utf-8'))


# 3.产出hash值
# print(m.hexdigest())
# sha后面的数字越大加密的算法越复杂
m1=hashlib.sha256()
m1.update('helloworldaaaaaaaaaaaaaaaaaaaa'.encode('utf-8'))
print(m1.hexdigest())

m2=hashlib.sha512()
m2.update('helloworldaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'.encode('utf-8'))
print(m2.hexdigest())




