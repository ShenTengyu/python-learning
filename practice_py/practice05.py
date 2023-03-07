"""
# 九九乘法表Version-01
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{} * {} = {}".format(j, i, j * i), end = '\t')
        if j == i:
            print("")
        j += 1
    i += 1
"""

"""
# for循环用法
name = 'heima'
for x in name:
    print(x, end = ' ')
"""

"""
# range的用法
for x in range(5):
    print(x, end = ' ')
print()
    
for x in range(6, 10):
    print(x, end = " ")
print()

for x in range(0, 100, 20):
    print(x, end = " ")
print()
"""

"""
# 九九乘法表Version-02
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} * {} ={} ".format(j, i, i * j), end = '')
    print()
"""

# 发工资
money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print("第{}位员工绩效分{}不够，不发放工资！".format(i, score))
        continue
    else :
        print("第{}位员工领取了1000元！".format(i))
        money -= 1000
    if money < 0:
        print("工资发放完毕！")
        break