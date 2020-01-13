# -*- coding: utf-8 -*-
from collections import deque
n,m = map(int, input().split())
edge = {}
for i in range(n):
    edge[i] = set()

for _ in range(m):
    v,u = map(int, input().split())
    v -= 1
    u -= 1
    edge[v].add(u)
    edge[u].add(v)

visited = [False]*n
res = 0
for i in range(n):
    if visited[i]:
        continue

    flag = True
    q = deque([(i,None)])
    while len(q)>0:
        v,prev = q.pop()
        visited[v] = True
        for u in edge[v]:
            if u!=prev and visited[u]:
                flag = False
            elif not visited[u]:
                q.append((u, v))
    if flag:
        res += 1

print(res)
