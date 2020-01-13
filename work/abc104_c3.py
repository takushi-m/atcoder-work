# -*- coding: utf-8 -*-
from itertools import combinations
inf = 10**9
d,g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

def score(comp):
    res = 0
    s = 0
    for i in comp:
        s += pc[i][1]
        s += pc[i][0]*100*(i+1)
        res += pc[i][0]

    if s>=g:
        return res

    for i in range(d-1,-1,-1):
        if i in comp:
            continue

        c = 0
        while c<pc[i][0]-1 and s<g:
            c += 1
            s += 100*(i+1)
        res += c

        if s>=g:
            return res
    return inf

res = inf
for r in range(d+1):
    for c in combinations(range(d),r):
        s = score(c)
        res = min(res, s)

print(res)