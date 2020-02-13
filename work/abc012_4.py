# -*- coding: utf-8 -*-
def warshallFloyd(d,n):
    inf = 10**18
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

n,m = map(int, input().split())
inf = 10**18
e = [[inf]*n for _ in range(n)]
for i in range(n):
    e[i][i] = 0
for _ in range(m):
    a,b,t = map(int, input().split())
    a -= 1
    b -= 1
    e[a][b] = t
    e[b][a] = t

d = warshallFloyd(e,n)

res = inf
for i in range(n):
    r = 0
    for j in range(n):
        if i==j:
            continue
        r = max(r,d[i][j])
    res = min(res, r)
print(res)