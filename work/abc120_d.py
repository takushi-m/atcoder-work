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

n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.reverse()
uf = UnionFind(n)
res = []
cur = n*(n-1)//2
for a,b in ab:
    res.append(cur)
    a -= 1
    b -= 1
    if uf.same(a,b):
        continue

    sa = uf.size(a)
    sb = uf.size(b)
    cur -= sa*sb
    uf.unite(a,b)

res.reverse()
for r in res:
    print(r)
