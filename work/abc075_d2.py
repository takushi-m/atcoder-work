# -*- coding: utf-8 -*-
from itertools import combinations

n,k = map(int, input().split())

xl = []
yl = []
xy = []
for _ in range(n):
    x,y = map(int, input().split())
    xl.append(x)
    yl.append(y)
    xy.append((x,y))
yl.sort()
xy.sort(key=lambda x:x[1])

res = None
for cx in combinations(xl, 2):
    x1,x2 = cx
    if x2>x1:
        x1,x2 = x2,x1

    for y2 in yl:
        cnt = 0
        for c in xy:
            x,y = c
            if x1>=x>=x2 and y>=y2:
                cnt += 1

            if cnt==k:
                y1 = y
                s = (x1-x2)*(y1-y2)
                if res is None:
                    res = s
                else:
                    res = min(res, s)
                break

print(res)
