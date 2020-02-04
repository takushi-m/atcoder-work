# 二部グラフの判定。連結でなくても良い
# eは隣接リスト。nは要素数
def is_bipartite(e,n):
    col = [-1]*n
    for s in range(n):
        if col[s]>=0:
            continue
        col[s] = 0
        q = [s]
        while len(q)>0:
            v = q.pop()
            c = col[v]
            for u in e[v]:
                if col[u]<0:
                    col[u] = (c+1)%2
                    q.append(u)
                else:
                    if c==col[u]:
                        return False
    return True

# 単一始点最短経路。2地点間ではなく、始点が一つで各点へのコストを計算する
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