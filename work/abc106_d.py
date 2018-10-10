# -*- coding: utf-8 -*-
n,m,q = map(int, input().split())

d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    l,r = map(int, input().split())
    d[l][r] += 1
for i in range(n,0,-1):
    for j in range(n):
        d[i][j+1] += d[i][j]
for j in range(n,0,-1):
    for i in range(n,0,-1):
        d[i-1][j] += d[i][j]

pq = []
for _ in range(q):
    p,q = map(int, input().split())
    pq.append([p,q])

# print(d)
for o in pq:
    print(d[o[0]][o[1]])
