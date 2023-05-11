n = 0
for i in range(101,201):
    for j in range(2,i):
            if i % j == 0 :
                break
            else  :
                if j == i-1:
                    n = n + 1
                    print(i)
print(n)