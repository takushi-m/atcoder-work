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

n,x,y = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n-1):
    g[i].append((i+1,1))
    g[i+1].append((i,1))
g[x-1].append((y-1,1))
g[y-1].append((x-1,1))
    

res = [0]*n
for i in range(n):
    d = dijkstra(g,n,i)
    for j in range(i+1,n):
        res[d[j]] += 1

for i in range(1,n):
    print(res[i])