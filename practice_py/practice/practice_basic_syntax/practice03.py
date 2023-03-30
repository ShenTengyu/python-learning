"""
# 基础运算
print("1 + 1 = ", 1 + 1)
print("1 - 1 = ", 1 - 1)
print("2 * 3 = ", 2 * 3)
print("4 / 2 = ", 4 / 2)    # 除法
print("3 // 2 = ", 3 // 2)  # 整除
print("3 ** 3 = ", 3 ** 3)
"""

"""
# 字符串的命名
name = '黑马'
print(type(name), name)

name = "黑马"
print(type(name), name)

name = ""\"黑马\"""
print(type(name), name)
"""

"""
# 字符串的拼接 
print("沈腾宇" + "加油")

name = "STY"
print("CSY + " + name + " = 爱情事业双丰收")

name = "黑马"
add = "郑州市"
tel = 18503806757
print(name + "在" + add + '等你！' + "请联系" + str(tel))
"""

# 字符串的占位、格式化
name1 = "黑马"
name2 = "白马"
message = "加油!%s、%s" % (name1, name2)
print(message)

num = 100
num1 = 13.14
message = "%s加油!我要考%d%%+%f" % (name1, num, num1)
print(message)

message = "%s加油!我要考%d%%+%.2f" % (name1, num, num1)
print(message)

message = "%s加油!我要考%d%%+%7.2f" % (name1, num, num1)
print(message)

# 字符串的格式化.format
name = "黑马"
year = 2000
print("{}生于{}年!".format(name, year)) #format方式一

print(f"{name}生于{year}年!")           #format方式二