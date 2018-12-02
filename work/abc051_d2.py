# -*- coding: utf-8 -*-
from copy import deepcopy
inf = 10**5
n,m = map(int, input().split())

edge = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    edge[i][i] = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a][b] = c
    edge[b][a] = c
edge_tmp = deepcopy(edge)

for k in range(n):
    for i in range(n):
        for j in range(n):
            edge[i][j] = min(edge[i][j], edge[i][k]+edge[k][j])

res = 0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if edge[i][j]!=edge_tmp[i][j] and edge_tmp[i][j]<inf:
            res += 1
print(res//2)
