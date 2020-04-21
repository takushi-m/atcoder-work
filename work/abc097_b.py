x = int(input())

res = 1
for i in range(2,x+1):
    p = 2
    while i**p<=x:
        res = max(res,i**p)
        p += 1
print(res)