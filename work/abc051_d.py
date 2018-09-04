# -*- coding: utf-8 -*-
INF = 10**10
n,m = map(int, input().split())
d = [[INF for _ in range(n)] for _ in range(n)]
el = []

for _ in range(m):
    a,b,c = map(int,input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    el.append([a-1,b-1,c])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                d[i][j] = 0

            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ret = 0
for ei in range(m):
    a = el[ei][0]
    b = el[ei][1]
    c = el[ei][2]
    flag = False
    for s in range(n):
        if d[s][a]+c==d[s][b]:
            flag = True
            break
    if not flag:
        ret += 1
print(ret)
