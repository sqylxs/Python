a = 0
b = 1
c = b
print(a)
print(b)
for i in range(0,10):
    print(a+b)
    b = a + c
    a = c
    c = b