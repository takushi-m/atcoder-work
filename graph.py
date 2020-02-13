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

# 単一始点最短経路。2地点間ではなく、始点が一つで各点へのコストを計算する
# eは隣接リストでe[v] = [(u1,cost1), (u2,cost2)]みたいな形を想定
# 辺の重みは負でも良い。負の閉路がある場合は第二戻り値でTrueを返す
# O(VE)
def bellmanFord(e,n,s):
    inf = 10**18
    d = [inf]*n
    d[s] = 0

    loop = False
    for i in range(n):
        updated = False
        for v in range(n):
            for u,c in e[v]:
                if d[v]!=inf and d[u]>d[v]+c:
                    d[u] = d[v]+c
                    updated = True
                    if i==n-1 and u==n-1:
                        loop = True
        if not updated:
            break
    return d,loop

# 全点対最短路
# dは隣接行列を想定。d自体を更新する
def warshallFloyd(d,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

# 最小全域木を求める。unionfindを利用
# eは隣接リストでe[v] = [(u1,cost1), (u2,cost2)]みたいな形を想定
# O(ElogV)
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]

    def same(self, x, y):
        return self.root(x)==self.root(y)

    def root(self, x):
        if self.par[x]<0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return

        if self.par[x]>self.par[y]:
            x,y = y,x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self,x):
        return -self.par[self.root(x)]

def kruskal(e,n):
    l = []
    for v in range(n):
        for u,c in e[v]:
            l.append((c,v,u))
    l.sort()

    uf = UnionFind(n)
    cost = 0
    res = []
    for c,v,u in l:
        if uf.same(v,u):
            continue
        res.append((v,u,c))
        cost += c
        uf.unite(v,u)
    return res,cost