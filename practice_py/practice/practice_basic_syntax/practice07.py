"""
# 正序、逆序输出列表
my_list = ['TOM', 'LILY', 'ROSE']
print(my_list[0])
print(my_list[1])
print(my_list[2])
print("------------")
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
"""

"""
# 嵌套列表
my_list = [['TOM', 'LILY', 'ROSE'], [0, 1, 2]]
print(my_list[0][0])
print(my_list[1][0])
"""

# list名.append(元素)

# list名.extend(容器)

# list名.insert(下标, 元素)

# del list名[下标]

# list名.pop(下标)    删除并取出原指定下标元素

# list名.remove(元素)

# list名.clear()

# list名.count(元素)

# list名.index(元素)

# len(list名)

"""
my_list = [21, 25, 21, 23, 22, 20]
print("原来的列表是:", end = '')
print(my_list)

my_list.append(31)
print("追加元素31后列表是:", end = '')
print(my_list)

my_list.extend([29, 33, 30])
print("追加新列表后列表是:", end = '')
print(my_list)

print('第一个元素是:', end = '')
print(my_list[0])

print('列表最后一个元素是:', end = '')
print(my_list[len(my_list) - 1])    
#print(my_list[-1])

print("元素31在列表下标为:", end = '')
print(my_list.index(31))
"""

"""
# 列表的遍历
my_list = ['g', 'o', 'o', 'd']
# 方法一
index = 0
while index < len(my_list):
    print(my_list[index],end = '')
    index += 1
print()
# 方法二
for index in my_list:
    print(index)
"""

"""
# 字符串的分割
my_str = "ithei ma cheng xuit yuan"
num = my_str.count("it")
print("my_str中有相应字符:{}个".format(num))

new_my_str = my_str.replace(' ', '|')   #str.replace()返回一个新的字符串，旧字符串依旧不变
print(new_my_str)

my_str_list = my_str.split(" ")         #str.split()依据所规定的字符分割成列表
print(my_str_list)
"""

# 序列(列表、元组、字符串)切片
    # my_list = [0, 1, 2, 3, 4, 5, 6]

    # result1 = my_list[1:4]
    # print(result1)

    # result2 = my_list[:]
    # print(result2)

    # result3 = my_list[0: 5: 2]
    # print(result3)

my_str = "学Python,来名师大讲堂,月薪过哇塞"

result1 = my_str[::-1]
print(result1)

result2 = my_str[::-1][:-8:-1]
print(result2)

result3 = my_str.split(",")
print(result3)
print(result3[1])
print(result3[1][::-1])

result4 = my_str.split(",")[1].replace("大", "da")[::-1]
print(result4)