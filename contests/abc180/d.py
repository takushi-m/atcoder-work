from math import ceil,log

x,y,a,b = map(int, input().split())


def calc(n):
    m = ceil((y-x*a**n)/b - 1)
    r1 = -1
    if x*a**n+b*m<y:
        r1 = n + m

    m = ceil((pow(y,1/n)-x)/b - 1)
    r2 = -1
    if x*a**n+b*m<y:
        r2 = n + m
    r2 = n + m

    return max(r1,r2)


N = ceil(log(y/x)/log(a))+10
res = 0
for n in range(N+1):
    res = max(res, calc(n))
print(res)