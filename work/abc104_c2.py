# -*- coding: utf-8 -*-
from itertools import combinations

d,g = map(int, input().split())
p = []
c = []
for _ in range(d):
    a,b = map(int, input().split())
    p.append(a)
    c.append(b)

res = 100*10
for i in range(d+1):
    for cc in combinations(range(d), i):
        t = 0
        s = 0
        for pi in cc:
            s += (pi+1)*100*p[pi] + c[pi]
            t += p[pi]
        if s<g:
            pi = max(set(range(d)) - set(cc))
            for j in range(1,p[pi]):
                s += (1+pi)*100
                t += 1
                if s>=g:
                    break
        if s>=g:
            res = min(res, t)
print(res)
