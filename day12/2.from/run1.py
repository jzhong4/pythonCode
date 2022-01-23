# 相对导入
# 相对导入
#       from .文件夹 import 模块
#       from ..文件夹 import 模块
#       from ...文件夹 import 模块

# 相对导入：参照当前所在文件的文件夹为起始开始查找，称之为相对导入
#     符合：.代表当前所在文件的文件夹 ..代表上一级文件夹 ...代表上一级的上一级文件夹
#     优点：导入更加简单
#     缺点：只能在导入包中的模块时才能使用，不能在执行文件中用
# 只能在导入包中的模块时才能使用，不能在执行文件中用
from dir1 import m1

m1.f1()