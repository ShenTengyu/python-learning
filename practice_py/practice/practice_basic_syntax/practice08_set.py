# set集合   去重、无序！
my_set = {'黑马', '白马', '红马', '绿马', '白马', '红马', '绿马', '白马', '红马', '绿马'}
print("my_set的类型是:{},内容为:{}".format(type(my_set), my_set))

# set.add()
my_set.add("皮马")
my_set.add("绿马")
print(my_set)

# set.remove(元素)  

# set.pop()     随机取出一个集合内的元素并删除

# set.clear()

# set3 = set1.difference(set2)      选择set1中有,但set2中没有的元素,创建新集合set3      set1、set2均没有影响

# set1.difference_update(set2)      在set1中消除set2中同样存在的元素        set1被修改

# set3 = set1.union(set2)           合并set1、set2,并创建新集合set3

# len(set)

# 集合遍历只能用for                    因为集合无序、不支持下标索引

my_list = ['黑马程序', '黑马', '黑马程', '无序', '黑马', '黑马程', '无序']
my_set = set()

for element in my_list:
    print('修改集合前为:{}'.format(my_set))
    my_set.add(element)
    print('修改集合后为:{}'.format(my_set))