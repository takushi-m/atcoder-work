# -*- coding: utf-8 -*-
n,m = map(int, input().split())
r = [[0]*n for _ in range(n)]
for i in range(n):
    r[i][i] = 1

for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    r[x][y] = 1
    r[y][x] = 1

res = 0
for i in range(1,2**n):
    grp = []
    for j in range(n):
        if i>>j&1==1:
            grp.append(j)
    flag = True
    for a in grp:
        for b in grp:
            flag = flag and r[a][b]==1
    if flag:
        res = max(res, len(grp))

print(res)
