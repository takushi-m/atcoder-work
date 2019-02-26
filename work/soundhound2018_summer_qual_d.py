# -*- coding: utf-8 -*-
import heapq
n,m,s,t = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,a,b = map(int, input().split())
    g[u].append((v,(a,b)))
    g[v].append((u,(a,b)))

inf = 10**18
def dijkstra(s, currency):
    d = [inf]*(n+1)
    d[s] = 0

    que = [(d[s],s)]
    heapq.heapify([que])
    while len(que)>0:
        _,v = heapq.heappop(que)
        for u,c in g[v]:
            if d[v]+c[currency]>=d[u]:
                continue
            d[u] = d[v]+c[currency]
            heapq.heappush(que, (d[u], u))
    return d

yen_c = dijkstra(s,0)
snuuk_c = dijkstra(t,1)

res = [0]*n
res[n-1] = yen_c[n] + snuuk_c[n]
for i in range(n-2,-1,-1):
    res[i] = min(res[i+1], yen_c[i+1]+snuuk_c[i+1])

for r in res:
    print(10**15-r)
