# -*- coding: utf-8 -*-
from collections import defaultdict
from operator import itemgetter

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
cd.sort()

m = defaultdict(lambda: [])
for i in range(n):
    for j in range(n):
        a,b = ab[i]
        c,d = cd[j]
        if a<c and b<d:
            m[j].append([i,a,b])

used = set()
res = 0
for j in range(n):
    if len(m[j])>0:
        l = sorted(m[j],key=itemgetter(2),reverse=True)
        for i,_,_ in l:
            if i not in used:
                used.add(i)
                res += 1
                break
print(res)