"""
# 基本异常捕获
try:
    f = open("E:\\src\\abcd.txt", "r", encoding="UTF-8")
except:
    print("原来程序出错，执行意外程序")
    f = open("E:\\src\\abcd.txt", "w", encoding="UTF-8")
"""

"""
# 捕获指定异常
try:
    print(nameerror)
except NameError as a:
    print("NameError被捕获了!")
    print(a)
    
# try:
#     # print(nameerror)
#     print(1 / 0)
# except NameError as a:
#     print("NameError被捕获了!")
"""
  
"""    
# 捕获多个异常
try:
    # 1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了NameError或者ZeroDivionError")
    print(e)
"""

"""
# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print("出现了Exception异常")
"""

"""
# 无异常时用else
try:
    print("Hello")
except Exception as e:
    print("出现异常!")
else:
    print("无异常出现!")
"""

# 无论有无异常都要执行的finally

"""
# 异常具有传递性
def func01():
    print("func01正在执行")
    num = 1 / 0
    print(num)
    
def func02():
    print("func02正在执行")
    func01()
    print("func02正在执行")
    
def main():
    try:
        func02()
    except Exception as e:
        print("出现异常了,异常信息是:{}".format(e))
    
main()
"""

"""
# 1.import
import time
print("请等待五秒!")
time.sleep(5)
print("等待五秒结束!")
"""

"""
# 2.from ... import ...
from time import sleep
print("你好")
sleep(3)
print("、、")
"""

"""
# 3.from ... import *
from time import *
print("另一种")
sleep(2)
print("引用")
"""

# 4.引用后用as起别名
from time import sleep as sl
print("起别名")
sl(2)
print("真有趣")

import time as t
print("起别名")
t.sleep(2)
print("真有趣")
