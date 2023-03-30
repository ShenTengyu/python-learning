"""
# if、elif、else等嵌套使用
if int(input("请输入你的年龄:")) >= 18:
    print("您已成年请补票10元,但如若VIP等级大于等于三级，亦可以免费！")
    if int(input("请输入您的VIP等级:")) >= 3:
        print("VIP请免费游玩!")
    else:
        print("SORRY!")
else :
    print("年龄不够，请享受游戏！")
"""

"""
# 猜测随机数-version-01
import random
num = random.randint(1,10)
if int(input("请输入您猜测的数字:")) == num:
    print("恭喜您一次就猜对了！")
elif int(input("请输入您猜测的数字:")) == num:
    print("恭喜您第二次猜对啦！")
elif int(input("请输入您猜测的数字:")) == num:
    print("恭喜您第三次猜对了！")
else :
    print("您猜错了！，正确数字为：",num)
"""

# 猜测随机数-version-02
import random
num = random.randint(1,10)
time = int(input("请输入您猜测的次数："))
i = 1
while i <= time:
    print("请输入您第{}次猜测的数字:".format(i))
    guess_num = int(input())
    if guess_num == num:
        print("恭喜您猜对了！")
    elif guess_num < num:
        print("请往大里猜测！")
    elif guess_num > num:
        print("请往小里猜测！")
    i += 1
print("您的猜测次数用完了！结束！")
    
        