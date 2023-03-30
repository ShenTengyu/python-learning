"""
# 相同名会被覆盖
from my_module01 import test
from my_module02 import test

test(1,2)
"""

# __main__变量
import my_package.my_module02 as my_module02

# __all__变量控制import * 内容(包中同样)

# 包
import my_package.my_module01
my_package.my_module01.test(1, 2)
