n = int(input())

def f(x):
    res = 0
    while x%2==0:
        x //= 2
        res += 1
    return res

cnt = 0
res = 1
for i in range(1,n+1):
    c = f(i)
    if c>cnt:
        cnt = c
        res = i

print(res)