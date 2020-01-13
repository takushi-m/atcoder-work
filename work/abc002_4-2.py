# -*- coding: utf-8 -*-
from itertools import combinations
n,m = map(int, input().split())

rel = {}
for i in range(n):
    rel[i] = set()
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1

    rel[x].add(y)
    rel[y].add(x)

res = 0
for r in range(1,n+1):
    for c in combinations(range(n),r):
        flag = True
        for x in c:
            for y in c:
                if x==y:
                    continue
                if y not in rel[x]:
                    flag = False
        if flag:
            res = max(res, len(c))

print(res)