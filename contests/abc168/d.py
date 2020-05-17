import heapq
# 単一始点最短経路。2地点間ではなく、始点が一つで各点へのコストを計算する
# eは隣接リストでe[v] = [(u1,cost1), (u2,cost2)]みたいな形を想定
# 辺の重みは正である必要がある
# O(ElogV)
def dijkstra(e,n,s):
    inf = 10**18
    d = [inf]*n
    prev = [s]*n
    d[s] = 0

    q = [(d[s],s)] # priority queueのソートキーが第一要素
    heapq.heapify([q])
    while len(q)>0:
        _,v = heapq.heappop(q)
        for u,c in e[v]:
            if d[v]+c>=d[u]:
                continue
            d[u] = d[v] + c
            prev[u] = v
            heapq.heappush(q, (d[u],u))
    return d, prev

n,m = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append((b,1))
    e[b].append((a,1))

d,prev = dijkstra(e,n,0)
if max(d)==10**18:
    print("No")
    exit()
print("Yes")
for i in range(1,n):
    print(prev[i]+1)