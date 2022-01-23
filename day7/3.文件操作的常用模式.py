''' *********
一 文件的打开模式
r:只读模式(默认)
w：只写模式
a: 只追加写模式

二 控制读写文件单位的方式（必须与r\w\a连用）
t： 文本模式(默认的)，一定要encoding参数
    优点：操作系统会将硬盘中二进制数字解码成unicode然后返回
    强调：只针对文本文件有效
b： 二进制模式（视频，图片），一定不能指定encoding参数
    优点：
'''
# rt:只读模式(默认)
# 1.当文件不存在，报错
# 2.当文件存在时，文件指针指向文件的开头
with open('a.txt',mode='rt',encoding='utf-8') as f:
    # res1 = f.read()
    # print('1>>>',res1)
    # 第一次读完了
    # res2 = f.read()
    # print('2>>>', res2)
    # 判断rt模块
    # 可读
    print(f.readable())
    # 不可写
    print(f.writable())
    # 文件里面有换行符
    # print 自带换行符\n，所有可以设置end
    # print(f.readline(),end='')
    # print(f.readline())

    # for循环遍历文件对象
    # for line in f:
    #     print(line, end='')

    L=[]
    # for line in f:
    #     L.append(line)
    #文件里面有换行符
    # print(L)
    # 一行代码搞定
    print(f.readlines())

# wt: 只写模式
# 当文件不存时，新建一个空文档
# with open('b.txt',mode='wt',encoding='utf-8') as f:
#     pass
# 当文件存在，清空文件内容，文件指针跑到文件的开头
with open('b.txt',mode='wt',encoding='utf-8') as f:
    #全部清空
    # 不可读
    print(f.readable())
    # 可写
    print(f.writable())
    # f.write(字符串)
    f.write('大海\n')
    f.write('大海\n')
    f.write('大海\n')
    # 一次性写多行
    f.write('111\n2222\n33333\n')
    # 把列表内容一行行写入
    info = ['大海\n','大海\n','大海\n']
    for line in info:
        f.write(line)
    # 一行代码搞定
    # writelines(列表)
    f.writelines(info)

# 三 at:只追加模式
# 当文件不存在，新建一个空文档，文件指针跑到文件的末尾
with open('c.txt',mode='at',encoding='utf-8') as f:
    pass
# 当文件存在时，文件指针跑到文件末尾
with open('c.txt',mode='at',encoding='utf-8') as f:
    # 不可读
    print(f.readable())
    # 可写
    print(f.writable())
    f.write('c大海\n')
    f.write('c大海\n')
    f.write('c大海\n')
with open('c.txt',mode='at',encoding='utf-8') as f:
    # 不可读
    print(f.readable())
    # 可写
    print(f.writable())
    f.write('a大海\n')
    f.write('a大海\n')
    f.write('a大海\n')

#wt模式文件打开不关闭的情况下，连续写入
#at模式关闭了下次打开是在文件末尾写，所以不会覆盖之前的内容

# 二级制文件b模式
# 图片和视频
# with open('1.png', mode='rb') as f:
#     data=f.read()
#     print(data)
#     print(type(data))
#
# with open('2.png', mode='wb') as f:
#     f.write(data)

# b模式，可以对文本文件操作，但是要解码
# decode 二进制解码成字符
# encode 字符编码成二进制
# 解码 读的时候转成字符

with open('b模式.txt',mode='rb') as f:
    data = f.read()
    print(data)
    print(type(data))
    print(data.decode('utf-8'))

# 编码 写得时候把字符转换成二级制写入
with open('wb模式.txt',mode='wb') as f:
    f.write('dahai\n'.encode('utf-8'))
    f.write('dahai\n'.encode('utf-8'))
    f.write('dahai\n'.encode('utf-8'))








