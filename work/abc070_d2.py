# -*- coding: utf-8 -*-
inf = 10**16
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b,c))
    edge[b].append((a,c))

q,k = map(int, input().split())
k -= 1

d = [inf for _ in range(n)]
d[k] = 0
stack = [k]
while len(stack)>0:
    v = stack.pop()
    for u,c in edge[v]:
        if d[u]==inf:
            d[u] = d[v]+c
            stack.append(u)

res = []
for _ in range(q):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    res.append(d[x]+d[y])

for c in res:
    print(c)
