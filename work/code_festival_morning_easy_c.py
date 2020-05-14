import heapq
# 単一始点最短経路。2地点間ではなく、始点が一つで各点へのコストを計算する
# eは隣接リストでe[v] = [(u1,cost1), (u2,cost2)]みたいな形を想定
# 辺の重みは正である必要がある
# O(ElogV)
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

n,m = map(int, input().split())
s,t = map(int, input().split())
s -= 1
t -= 1

e = [[] for _ in range(n)]
for _ in range(m):
    x,y,d = map(int, input().split())
    x -= 1
    y -= 1
    e[x].append((y,d))
    e[y].append((x,d))

d1 = dijkstra(e,n,s)
d2 = dijkstra(e,n,t)
for u in range(n):
    if d1[u]<10**18 and d1[u]==d2[u]:
        print(u+1)
        exit()
print(-1)
