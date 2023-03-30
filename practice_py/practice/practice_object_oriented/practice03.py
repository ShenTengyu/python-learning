"""
# 闭包
def outer(logo):
    
    def inner(msg):
        print("<{}>{}<{}>".format(logo, msg, logo))
    
    return inner

fn1 = outer("LOGO")
fn1("这是内容")

fn2 = outer("LOGO")
fn2("白昼向你问好")
"""

"""
# nonlocal关键字
def outer(num1):
    
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)
        
    return inner

fn = outer(10)
fn(10)
fn(20)
"""

"""
# 闭包实现ATM
def account_create(initial_amount = 0):
    
    def inner(increase_amount, deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += increase_amount
            print("存款后，用户余额为:{}元".format(initial_amount))
        else:
            initial_amount -= increase_amount
            print("取款后，用户余额为:{}元".format(initial_amount))
        
    return inner

account = account_create()
account(100)
account(100, False)
"""

"""
# 装饰器(基础写法)
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))
    
def outer(func):
    
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
        
    return inner

fn = outer(sleep)
fn()
"""

# 装饰器(高级)
def outer(func):
    
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
        
    return inner

@outer

def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))
    
sleep()
    