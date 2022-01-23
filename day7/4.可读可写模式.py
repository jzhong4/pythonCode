# 可读可写 - 了解
# r+t
# w+t
# a+t

# r+t
# 1.当文件不存在时，会报错
# 2.当文件存在时，文件指针指向文件的开头
# 3.多了个末尾写
with open('可读可写r+t模式.txt',mode='r+t',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    msg = f.readline()
    print(msg)
    f.write('xxxx')

# w+t
# 当文件不存时，新建一个空文档
# 当文件存在，清空文件内容，文件指针跑到文件的开头
# 可以读
with open('可读可写w+t模式.txt',mode='w+t',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('aaaaaaa\n')
    f.write('bbbbbbb\n') #指针跑到最后

    # 指针移动seek (移动的字节数，开头开始0)
    # 从开头移动0
    f.seek(0,0)
    print(f.readline())
    f.write('cccccccc\n')

# a+t 第二次打开时候也是在末尾写
# a和w区别
with open('可读可写a+t模式.txt',mode='a+t',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('aaaaaaa\n')
    f.write('bbbbbbb\n') #指针跑到最后

    # 指针移动seek (移动的字节数，开头开始0)
    # 从开头移动0
    f.seek(0,0)
    print(f.readline())
    f.write('cccccccc\n')

# 图片视频用不上
# r+b w+b a+b 规律和 r+t w+t a+t
# 乱掉文件打不开