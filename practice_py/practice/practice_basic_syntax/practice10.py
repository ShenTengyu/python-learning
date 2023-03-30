"""
# 函数多个返回值
def fun_multi_return():
    return 1,2
x, y = fun_multi_return()
print("函数的返回值为:{}、{}".format(x, y))
"""

"""
# 函数的多种传参

# 1.位置参数

# 2.关键字参数

# 3.缺省参数(默认值)


# 4.*参数名
def my_func(*args):
    print("参数为:{}".format(args))

my_func()
my_func("hello")
my_func("good", "morning")

# 5.**参数名
def my_func(**args):
    print("参数为:{}".format(args))
    
my_func(STY = 1, CSY = 2)
"""

"""
# 一个函数作为另一个函数的参数
def my_func(cmopute):
    print("compute的类型是:{},内容为:{}".format(type(compute), compute(1, 2)))
    
def compute(x, y):
    return x + y

my_func(compute)
"""

# lambda匿名函数
def test_func(compute):
    result = compute(1, 2)
    print("结果为:{}".format(result))

test_func(lambda x, y:x + y)