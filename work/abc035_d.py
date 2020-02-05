import heapq
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


n,m,t = map(int, input().split())
al = list(map(int, input().split()))
ef = [[] for _ in range(n)]
er = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    ef[a].append((b,c))
    er[b].append((a,c))

df = dijkstra(ef,n,0)
dr = dijkstra(er,n,0)

res = -1
for i in range(n):
    if df[i]+dr[i]<t:
        res = max(res, (t-df[i]-dr[i])*al[i])
print(res)