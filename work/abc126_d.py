# -*- coding: utf-8 -*-
from collections import defaultdict
n = int(input())
e = defaultdict(lambda: [])

for _ in range(n-1):
    v,u,w = map(int, input().split())
    v -= 1
    u -= 1
    e[v].append((u,w))
    e[u].append((v,w))

col = [-1]*n
q = [0]
col[0] = 0
while len(q)>0:
    v = q.pop()
    for u,w in e[v]:
        if col[u]<0:
            if w%2==1:
                col[u] = (col[v]+1)%2
            else:
                col[u] = col[v]
            q.append(u)

print(*col)