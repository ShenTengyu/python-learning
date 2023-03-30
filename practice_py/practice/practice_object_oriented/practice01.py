"""
# 初识面向对象编程
class Student:
    name = None
    age = None
    
    def say_hi(self):
        print("你好!,我叫{},今年{}岁了!".format(self.name, self.age))
        
    def say_wo(self, mes):
        print("WOW!{}".format(mes))
        
# student01
student01 = Student()

student01.age = 18
student01.name = "周润发"
student01.say_hi()
student01.say_wo("你很不错哦")

# student02
student02 = Student()

student02.age = 23
student02.name = "李德华"
student02.say_hi()
student02.say_wo("不错哦!")
"""

"""
# 闹钟
class Clock:
    id = None
    price = None
    
    def ring(self):
        import winsound
        winsound.Beep(1000, 1000)
        
clock01 = Clock()
clock01.id = "00798"
clock01.price = 18
clock01.ring()

clock02 = Clock()
clock02.id = "00415"
clock02.price = 29
clock02.ring()
"""

"""
# 构造函数__init__()
class Student:
    name = None
    age = None
    tel = None
    
    def __init__(self, name, age, tel) -> None:
        self.name = name
        self.age = age
        self.tel = tel
        print("构造函数执行完成!")
        
student01 = Student("STY", 20, "111158")
print(student01.name)
print(student01.age)
print(student01.tel)
"""

"""
# 内置方法

# __str__()

# __lt__()

# __le__()

# __eq__()
"""

"""
# 私有变量、私有函数
class Phone:
    __is_5g_enable = False
    
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G网络开启")
        else:
            print("5G网络关闭")
            
    def call_by_5G(self):
        self.__check_5g()
        print("正在通话中")
        
phone01 = Phone()
phone01.call_by_5G()
"""

"""
# 单继承、多继承

# 子类对父类的 复写

# 父类被复写后 仍想继续使用父类中的属性、方法

class Phone:
    IMEI = None         # 序列号
    producer = "ITCAST" # 厂商
    
    def call_by_5G(self):
        print("父类 的函数调用")
        print(f"厂商为:{self.producer}")

class Phone_Plus(Phone):
    producer = "STY"
        
    def call_by_5G(self):
        print(f"弗雷德厂商是{Phone.IMEI}")
        print("子类 的函数调用")
        return super().call_by_5G() 
    
phone = Phone_Plus()
phone.call_by_5G()
print(phone.producer)
"""

# 基础类型注解
var_1: int = 10
var_2: str = "STY"
var_3: bool = True

# 类对象类型注解
class Student:
    pass

stu: Student = Student()

# 容器类型注解
my_list: list = [1, 2, 3]
my_dict: dict = {"STY": 19}
my_tuple: tuple = (1 ,2, 3)

# 容器 详细 类型注解
my_list: list[int] = [1, 2, 3]
my_dict: dict[str, int] = {"STY": 19}
my_tuple: tuple[int, int, int] = (1 ,2, 3)

# 注释中进行类型注解

# 类型注释仅仅是注释 不影响正确与否
my_dict: list[int] = ["1", "2", "3"]
var_1: int = "sty"

# 函数形参类型注释、函数返回值类型注释
def my_func(data: list) -> list:
    return data 

my_func()

# Union类型进行综合注释
from typing import Union
my_list: list[Union[str, int]] = [1, 2, "sty"]