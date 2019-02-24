# -*- coding: utf-8 -*-
from itertools import product
n,a,b,c = map(int, input().split())
ll = [int(input()) for _ in range(n)]

res = 10**10
for t in product([0,1,2,3], repeat=n):
    x = [0,0,0]
    y = [0,0,0]
    for i in range(len(t)):
        if t[i]==3:
            continue
        x[t[i]] += ll[i]
        y[t[i]] += 1
    if min(x)==0:
        continue
    for i in range(3):
        if y[i]>=2:
            y[i] -= 1
        elif y[i]==1:
            y[i] = 0

    x.sort()
    tmp = abs(a-x[2])+abs(b-x[1])+abs(c-x[0])+10*sum(y)
    res = min(res, tmp)

print(res)
