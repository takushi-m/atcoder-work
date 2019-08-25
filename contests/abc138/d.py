# -*- coding: utf-8 -*-
n,q = map(int, input().split())

cnt = [0 for _ in range(n)]

edge = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)

for _ in range(q):
    p,x = map(int, input().split())
    cnt[p-1] += x

for v in range(n):
    for u in edge[v]:
        cnt[u] += cnt[v]

print(" ".join([str(x) for x in cnt]))
