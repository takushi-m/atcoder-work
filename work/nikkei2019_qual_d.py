# -*- coding: utf-8 -*-
n,m = map(int, input().split())
edge = {}
inl = [0]*(n+1)
for _ in range(n-1+m):
    a,b = map(int, input().split())
    if a not in edge:
        edge[a] = []
    edge[a].append(b)
    inl[b] += 1

s = []
for v in range(1,n+1):
    if inl[v]==0:
        s.append(v)

l = []
res = [0]*(n+1)
while len(s)>0:
    v = s.pop()
    l.append(v)
    if not v in edge:
        continue
    for u in edge[v]:
        inl[u] -= 1
        if inl[u]==0:
            res[u] = v
            s.append(u)

for i in range(1,n+1):
    print(res[i])
