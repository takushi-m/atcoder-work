# -*- coding: utf-8 -*-

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x]==x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x==y:
            return

        if self.rank[x]<self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x]==self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x)==self.find(y)

n,m = map(int, input().split())
p = [int(x) for x in input().split()]
uf = UnionFind(n+1)
for _ in range(m):
    x,y = map(int, input().split())
    uf.unite(x,y)

cnt = 0
for i in range(1,n+1):
    if uf.same(i,p[i-1]):
        cnt += 1

print(cnt)
