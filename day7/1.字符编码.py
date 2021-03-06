'''
什么是字符编码

计算机只认识数字(二进制0101),其他的数字10进制都是通过二级制转换过来的
如何让计算机读懂人类的字符？
必须经过一个过程：
# 字符 ----翻译---数字
这个过程实际就是一个字符如何对应一个特定数字的标准，这个标准称之为字符编码

字符编码的发展史与分类？
计算机由美国人发明的。
英文编码
ASCII ascii用**1个字节(8位二进制)代表一个二进制字符 01010100
8bit = 1Bytes
1024Bytes = 1KB
1024KB = 1MB
1024MB = 1GB
1024GB = 1TB
1024TB = 1PB
最早的字符编码位ASCII，只规定了英文字母数字和一些特殊字符与数字的对应关系
所以ASCII码最多只能表示256个符号，即2**8=256
ASCII码没法表示中文，一个汉字要多个字节去表示，位数越多，代表变化就多，这样，就可以尽可能
多的表达出不同的汉字

gb2312
所以中国人规定了自己的标准gb2312编码
规定了包含中文在内的字符 --》数字的对应关系

GB2312的出现，基本满足了汉字的计算机处理需要，
但对于人名，古汉语等方面出现的罕用字，GB2312不能处理，这导致GBK汉字字符集出现
GBK的诞生 **3个字节 01010100 01010100 01010100 2**24

日本
Shift_JIS编码

韩国
Euc-kr编码

Unicode 诞生，它是在内存里面的
用2个字节代表一个字符，用4个字节代表生僻字
所以unicode兼容ascii，也兼容万国
但是如果我们的文档通篇是英文的，使用unicode会比ascii耗费多一倍空间，在存储和传输上十分低效

UTF-8 它在硬盘里面
UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用英文字母被编码成1个字节，
汉字通常是3个字节，生僻字4-6个字节
字符  ASCII          Unicode              UTF-8
A   01000001   00000000 01000001         01000001
中  没有     11100100 01001110 00101101  11100100 01001110 00101101
简单说英文字母UTF-8使用和ASCII对应关系一样
而中文UTF-8使用Unicode对应关系

Unicode和UTF-8关系
1. 在存入磁盘是，需要将unicode转化成一种更为精准的格式，utf-8，将数据量控制到最精简
2. 在读入内存时，需要将utf-8转成unicode，所以我们需要明确：内存中使用unicode是为了
兼容万国软件，即便硬盘中有各国编码编写的软件，unicode也有对应的映射关系，但是现在的开发中，
程序员普遍使用utf-8编码了，估计在将来的某一天等所有老的软件都淘汰掉了情况下啊，就可以变成
内存unicode《---》硬盘utf-8的形式了

'''