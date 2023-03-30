"""
# dict的定义
my_dict1 = {"STY":311904010520, "CSY":311904010978, "WLH":311904010708}
my_dict2 = {}
my_dict3 = dict()

print("my_dict1的类型是:{},内容为:{}".format(type(my_dict1), my_dict1))
print("my_dict2的类型是:{},内容为:{}".format(type(my_dict2), my_dict2))
print("my_dict3的类型是:{},内容为:{}".format(type(my_dict3), my_dict3))
"""

# dict和set一样去重 

"""
# Key:Value
my_dict1 = {"STY":311904010520, "CSY":311904010978, "WLH":311904010708}
print("STY的学号为:{}".format(my_dict1["STY"]))
"""

"""
# dict可以嵌套
my_dict1 = {
    "STY":{"语文":99, "数学":100, "英语":500},
    "CSU":{"语文":99, "数学":100, "英语":500},
    "CSY":{"语文":99, "数学":100, "英语":500}
}
print("所有学生成绩为:{}".format(my_dict1))

print("STY的语文成绩为:{}".format(my_dict1["STY"]["语文"]))
print("STY的数学成绩为:{}".format(my_dict1["STY"]["数学"]))
print("STY的英语成绩为:{}".format(my_dict1["STY"]["英语"]))
"""

"""
# dict的操作
my_dict = {"周星驰":99, "成龙":10, "李连杰":50}
# dict新增、更改元素

my_dict["王尼玛"] = 66
print(my_dict)

my_dict["周星驰"] = 100
print(my_dict)

# dict删除元素
score = my_dict.pop("周星驰")
print("移除周星驰后字典为:{}\n周星驰的相应值为:{}".format(my_dict, score))

# dict.clear()

# dict.keys()
print("my_dict的全部keys为:{}".format(my_dict.keys()))

# 遍历dict
for key in my_dict.keys():
    print("my_dict中的key为:{},相应的value为:{}".format(key, my_dict[key]))
    
# len(dict)
"""

info_dict = {
    "王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
    "周星驰": {"部门": "市场部", "工资": 5000, "级别": 2},
    "李连杰": {"部门": "市场部", "工资": 7000, "级别": 4},
    "王尼玛": {"部门": "科技部", "工资": 4000, "级别": 1}
}

print("升级前的结果为:{}".format(info_dict))

for key in info_dict:
    if info_dict[key]['级别'] == 1:
        employee_info_dict = info_dict[key]
        employee_info_dict["级别"] += 1
        employee_info_dict["工资"] += 1000
        
info_dict[key] = employee_info_dict

print("升级后的结果为:{}".format(info_dict))