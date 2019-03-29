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

n,k,l = map(int, input().split())
road = UnionFind(n)
for _ in range(k):
    p,q = map(int, input().split())
    road.unite(p-1, q-1)

rail = UnionFind(n)
for _ in range(l):
    r,s = map(int, input().split())
    rail.unite(r-1, s-1)

d = {}
for i in range(n):
    x = (road.root(i), rail.root(i))
    if x not in d:
        d[x] = 0
    d[x] +=1

res = [d[(road.root(i), rail.root(i))] for i in range(n)]
print(*res)
