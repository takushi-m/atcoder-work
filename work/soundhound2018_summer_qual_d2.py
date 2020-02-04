# -*- coding: utf-8 -*-
import heapq
n,m,s,t = map(int, input().split())
s -= 1
t -= 1
ea = [[] for _ in range(n)]
eb = [[] for _ in range(n)]
for _ in range(m):
    v,u,a,b = map(int, input().split())
    v -= 1
    u -= 1
    ea[v].append((u,a))
    ea[u].append((v,a))
    eb[v].append((u,b))
    eb[u].append((v,b))
    


def dijkstra(e,n,s):
    inf = 10**18
    d = [inf]*n
    d[s] = 0

    q = [(d[s],s)] # priority queueのソートキーが第一要素
    heapq.heapify([q])
    while len(q)>0:
        _,v = heapq.heappop(q)
        for u,c in e[v]:
            if d[v]+c>=d[u]:
                continue
            d[u] = d[v] + c
            heapq.heappush(q, (d[u],u))
    return d


da = dijkstra(ea,n,s)
db = dijkstra(eb,n,t)
res = [0]*n
res[n-1] = da[n-1]+db[n-1]
for i in range(n-2,-1,-1):
    res[i] = min(res[i+1], da[i]+db[i])

for r in res:
    print(10**15 - r)