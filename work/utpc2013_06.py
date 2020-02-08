# -*- coding: utf-8 -*-
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

def kruskal(l,n):
    l.sort()

    uf = UnionFind(n)
    cost = 0
    res = []
    for c,v,u in l:
        if uf.same(v,u):
            continue
        res.append((c,v,u))
        cost += c
        uf.unite(v,u)
    return res,cost


n,m = map(int, input().split())
e = [[0]*n for _ in range(n)]
for _ in range(m):
    v,u,w = map(int, input().split())
    e[v][u] = w
    e[u][v] = w

q = int(input())
uf = UnionFind(n)
edges = [[] for _ in range(n)]
for _ in range(q):
    p,q = map(int, input().split())

    pp = uf.root(p)
    qq = uf.root(q)
    candidate = []
    for c in edges[pp]:
        candidate.append(c)
    for c in edges[qq]:
        candidate.append(c)

    gp = [i for i in range(n) if uf.root(i)==pp]
    gq = [i for i in range(n) if uf.root(i)==qq]
    for v in gp:
        for u in gq:
            if e[v][u]>0:
                candidate.append((e[v][u],v,u))
    uf.unite(p,q)
    
    edges[uf.root(p)],c = kruskal(candidate, n)
    if c>0:
        print(c)
    else:
        print("IMPOSSIBLE")
    