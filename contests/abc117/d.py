# -*- coding: utf-8 -*-
n,k = map(int, input().split())
al = list(map(int, input().split()))

def f(x):
    res = 0
    for a in al:
        res += x^a
    return res

# for x in range(k+1):
#     print(x,f(x))

cs = []
mi = 0
while (1<<mi)<=k:
    s0 = 0
    s1 = 0
    for a in al:
        b = (a>>mi)&1
        if b==1:
            s1 += 1
        else:
            s0 += 1
    cs.append((s0,s1))
    mi += 1
mi += 1
res = 0
for idx in range(mi):
    x = 0
    for i in range(mi):
        if i>idx:
            x += k&(1<<i)
        elif i==idx:
            pass
        else:
            if cs[i][0]>cs[i][1]:
                x += 1<<i
    res = max(res, f(x))

print(res)
