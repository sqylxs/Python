# append
# insert
# pop
# [:]
#join
#str将整数、浮点数、列表、元组、字典和集合转换为字符串类型   ord返回对应的 ASCII 数值
print(str(13524))
print(ord("a"))
a = "abcdefg"
print(a[0:-2])
print(a)
b = [1,2,"abc",[1,2]]
c = b.pop()
print(c)
print(b)
b.append(5)
b.insert(2,2)
print(b)
# in
print("a" in a)
s = [8,7,5,4,6,5,2]
# ?.sort()
# sum()
# max()
# min()
# ?.reverse()  将字符逆序输出
print(s)
s.sort()
print(s)
print(sum(s))
print(max(s))
print(min(s))
s.reverse()
print(s)
#lower 函数全部变成小写
#eval 将字符串智能转换
# n = input().split(',或 ') 转化为列表，去掉空格或逗号
try:
    a = int(input())
except:
    print('aaa')

# list基本使用
Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])   # 输出 Monday

#list 搜索
print(Weekday.index("Wednesday"))

#list 增加元素
Weekday.append("new")
print(Weekday)

# list 删除
Weekday.remove("Thursday")
print(Weekday)