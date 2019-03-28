# -*- coding: utf-8 -*-
from itertools import permutations

n,m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

res = 0
for path in permutations(range(n)):
    if path[0]!=0:
        continue

    add = 1
    for i in range(n-1):
        if path[i+1] not in edge[path[i]]:
            add = 0
    res += add

print(res)
