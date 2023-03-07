# 整数、浮点数转换为字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(13.14)
print(type(float_str), float_str)

# 字符串转换为数字
num = int("11")
print(type(num), num)

num = float("11")
print(type(num), num)

# 字符串内需要是数字才可以转换为数字！
"""num = int("sh")
print(type(num), num)"""

# 整数->浮点数
num = float(11)
print(type(num), num)

# 浮点数->整数
num = int(13.14)
print(type(num), num)