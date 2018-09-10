# -*- coding: utf-8 -*-
from itertools import permutations

inf = 10**30
n,m,r = map(int, input().split())
rr = [int(x) for x in input().split()]
a = []
b = []
c = []
d = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    aa,bb,cc = map(int, input().split())
    aa -= 1
    bb -= 1
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d[aa][aa] = 0
    d[bb][bb] = 0
    d[aa][bb] = cc
    d[bb][aa] = cc

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ret = inf
for l in permutations(rr):
    tmp = 0
    for i in range(r-1):
        tmp += d[l[i]-1][l[i+1]-1]
    if tmp < ret:
        ret = tmp

print(ret)
