p = int(input())

def fac(n):
    r = 1
    for x in range(1,n+1):
        r *= x
    return r

c = [fac(i) for i in range(10,0,-1)]

res = 0
for x in c:
    if p%x==0:
        res += p//x
        break
    else:
        res += p//x
        p = p%x
print(res)
    