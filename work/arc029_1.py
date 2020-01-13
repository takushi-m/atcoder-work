# -*- coding: utf-8 -*-
from itertools import combinations

n = int(input())
tl = [int(input()) for _ in range(n)]

res = 10**9
for r in range(n):
    for c in combinations(range(n),r):
        t1 = 0
        t2 = 0
        for i in range(n):
            if i in c:
                t1 += tl[i]
            else:
                t2 += tl[i]
        
        res = min(res, max(t1,t2))

print(res)