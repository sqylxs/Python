x = int(input())
y = int(input())
z = int(input())
for i in range (0,3):
    if x > y :
        n = x
        x = y
        y = n
    elif x > z :
        n = x
        x = z
        z = n 
    elif y > z:
        n = y
        y = z
        z = n
print(x,y,z)