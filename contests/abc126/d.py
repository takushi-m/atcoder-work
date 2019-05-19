# -*- coding: utf-8 -*-
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v,w))
    edge[v].append((u,w))

res = [-1]*n
res[0] = 0
q = [0]
while len(q)>0:
    u = q.pop(0)
    if len(edge[u])==0:
        continue

    for v,w in edge[u]:
        if res[v]!=-1:
            continue
        if w%2==0:
            res[v] = res[u]
        else:
            res[v] = (res[u]+1)%2
        q.append(v)

for r in res:
    print(r)
