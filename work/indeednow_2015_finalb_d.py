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

h,w = map(int, input().split())
sw,sh = map(int, input().split())
gw,gh = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]

q = []
for hi in range(h):
    for wi in range(w):
        for dh,dw in [[1,0],[0,1],[-1,0],[0,-1]]:
            if h>hi+dh>=0 and w>wi+dw>=0:
                x = p[hi][wi]
                y = p[hi+dh][wi+dw]
                q.append((x*y, w*hi+wi, w*(hi+dh)+wi+dw))
q.sort(reverse=True)

uf = UnionFind(h*w)
point = 0
for c,v,u in q:
    if uf.same(v,u):
        continue
    point += c
    uf.unite(v,u)

print(point + sum([sum(p[hi]) for hi in range(h)]))