# 方式一： 使用print()直接输出类型信息
print(type(666))
print(type(13.14))
print(type("china"))
# 方式二： 使用变量存储type()结果
int_type = type(666)
float_type = type(13.14)
str_type = type("china")
print(int_type)
print(float_type)
print(str_type)
# 方式三： 使用变量存储
name = "黑马"
type = type(name)
print(type)
