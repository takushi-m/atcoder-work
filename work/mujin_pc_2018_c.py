# -*- coding: utf-8 -*-
n,m = map(int, input().split())
s = [list(input()) for _ in range(n)]

l = [[0]*m for _ in range(n)]
r = [[0]*m for _ in range(n)]
u = [[0]*m for _ in range(n)]
d = [[0]*m for _ in range(n)]

for ni in range(n):
    for mi in range(m):
        if s[ni][mi]=="#":
            continue
        if mi-1>=0 and s[ni][mi-1]==".":
            l[ni][mi] += l[ni][mi-1]+1
        if ni-1>=0 and s[ni-1][mi]==".":
            u[ni][mi] += u[ni-1][mi]+1
for ni in range(n-1,-1,-1):
    for mi in range(m-1,-1,-1):
        if s[ni][mi]=="#":
            continue
        if mi+1<m and s[ni][mi+1]==".":
            r[ni][mi] += r[ni][mi+1]+1
        if ni+1<n and s[ni+1][mi]==".":
            d[ni][mi] += d[ni+1][mi]+1

res = 0
for ni in range(n):
    for mi in range(m):
        res += (u[ni][mi]+d[ni][mi])*(l[ni][mi]+r[ni][mi])
print(res)
