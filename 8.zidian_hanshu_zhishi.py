#字典

# dist = {
#     "a" : 1,
#     "b" : "asdfghjk",
#     "k" : [1,2,13,"asdfg"],
#     "o" : {
#         "a" : 1,
#         "b" : "asdfghjk",
#         "k" : [1,2,13,"asdfg"]
#     }

# }
# print(dist.get("f",-1))
# dist["asd"] = 56
# print(dist["a"])
# print(dist)
# for i in dist.keys():
#     print(dist[i])
# print(type(dist))
# print(dist.pop("o"))

# 函数

# def func(a,b="asd"): #可以有初始值
#     # pass 占位
#     print(a+b)
# func(2,3)
# print(func("a","b"))

#递归

# def func(n):
#     if n == 0:
#         return 0
#     else:
#         return func(n-1) + n
# print(func(5))

#递归求阶乘

def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)
print(func(999))

# 数值运算
print (5 + 4)  # 加法   输出 9
print (4.3 - 2) # 减法   输出 2.3
print (3 * 7)  # 乘法  输出 21
print (2 / 4)  # 除法，得到一个浮点数    输出 0.5
print (2 // 4) # 除法，得到一个整数 输出 0
print (17 % 3) # 取余   输出 2
print (2 ** 5) # 乘方  输出 32

# 不换行
x="a"
y="b"
print(x, end=' ')
print(y, end=' ')

# 科学计数法表示
# 2.5e2 = 2.5 x 102 = 250、

# 数字类型转换

# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。额外说明

