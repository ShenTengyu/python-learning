"""
# 多态
class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("汪汪!")

class Cat(Animal):
    def speak(self):
        print("喵喵!")
        
def my_func(animal: Animal):
    animal.speak()
    
dog = Dog()
cat = Cat()

my_func(dog)
my_func(cat)
"""

# 抽象类
class Air_Conditionner:
    def cool_wind(self):
        # 空调制冷
        pass
    
    def hot_wind(self):
        # 空调制热
        pass
    
    def swing_wind(self):
        # 空调摆风
        pass
    
    
class Midea_Air_Conditioner(Air_Conditionner):
    def cool_wind(self):
        # 空调制冷
        print("Midea空调冷风")
    
    def hot_wind(self):
        # 空调制热
        print("Midea空调热风")
    
    def swing_wind(self):
        # 空调摆风
        print("Midea空调摆风")
        
class Gree_Air_Conditioner(Air_Conditionner):
    def cool_wind(self):
        # 空调制冷
        print("Gree空调冷风")
    
    def hot_wind(self):
        # 空调制热
        print("Gree空调热风")
    
    def swing_wind(self):
        # 空调摆风
        print("Gree空调摆风")
        
def make_cool_wind(ac: Air_Conditionner):
    ac.cool_wind()
    
air01 = Midea_Air_Conditioner()
air02 = Gree_Air_Conditioner()

make_cool_wind(air01)
make_cool_wind(air02)