# -*- coding: utf-8 -*-
from itertools import combinations

line = input().split(" ")
d = int(line[0])
g = int(line[1])

p = []
c = []
for _ in range(d):
    line = input().split(" ")
    p.append(int(line[0]))
    c.append(int(line[1]))

ret = 10000
for sel in range(0,d+1):
    for s in combinations(range(d),sel):
        score = 0
        num = 0
        for si in s:
            score += (si+1)*100*p[si] + c[si]
            num += p[si]
        if score>=g:
            if num<ret:
                ret = num
            continue

        r = set(range(d)) - set(s)
        if len(r)==0:
            continue

        si = max(r)
        for pi in range(p[si]):
            score += (si+1)*100
            num += 1
            if score>=g and num<ret:
                ret = num

print(ret)
