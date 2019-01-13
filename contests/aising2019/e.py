# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))
edge = [-1 for _ in range(n)]

for _ in range(n-1):
    u,v = map(int, input().split())
    if u>v:
        u,v = v,u
    edge[u-1] = v-1

xl = []
i = 0
for _ in range(n)
    xl.append(al[i])
    i = edge[i]

print(xl)
