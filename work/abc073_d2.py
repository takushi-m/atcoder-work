# -*- coding: utf-8 -*-
from itertools import permutations

inf = 10**6
n,m,r = map(int, input().split())
rl = list(map(int, input().split()))
edge = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a][b] = c
    edge[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                edge[i][i] = 0
            else:
                edge[i][j] = min(edge[i][j], edge[i][k]+edge[k][j])

res = inf
for c in permutations(rl, r):
    tmp = 0
    for i in range(r-1):
        tmp += edge[c[i]-1][c[i+1]-1]
    res = min(res, tmp)

print(res)
