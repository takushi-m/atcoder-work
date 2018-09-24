# -*- coding: utf-8 -*-
from itertools import combinations

n,k = map(int, input().split())
pary = []
xary = []
yary = []
for _ in range(n):
    x,y = map(int, input().split())
    pary.append([x,y])
    xary.append(x)
    yary.append(y)

ret = None
for x in combinations(range(n),2):
    for y in combinations(range(n),2):
        xc = [xary[x[0]], xary[x[1]]]
        yc = [yary[y[0]], yary[y[1]]]
        cnt = 0
        for p in pary:
            if (min(xc[0],xc[1])<=p[0]<=max(xc[0],xc[1])
                and min(yc[0],yc[1])<=p[1]<=max(yc[0],yc[1])):
                cnt += 1
            if cnt==k:
                break
        if cnt>=k:
            s = abs(xc[0]-xc[1]) * (abs(yc[0]-yc[1]))
            if ret is None:
                ret = s
            else:
                ret = min(ret,s)

print(ret)
