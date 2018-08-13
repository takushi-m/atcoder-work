# coding=utf-8


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


n = 100
k = 7
infos = [
    (1,101,1) # (type, x, y)
    ,(2,1,2)
    ,(2,2,3)
    ,(2,3,3)
    ,(1,1,3)
    ,(2,3,1)
    ,(1,5,5)
]


uf = UnionFind(3*n)
ans = 0
for info in infos:
    t = info[0]
    x = info[1]-1
    y = info[2]-1

    if x<0 or x>=n or y<0 or y>=n:
        ans += 1
        continue

    if t==1:
        if uf.same(x,y+n) or uf.same(x,y+2*n):
            ans += 1
        else:
            uf.unite(x,y)
            uf.unite(x+n,y+n)
            uf.unite(x+2*n,y+2*n)
    else:
        if uf.same(x,y) or uf.same(x,y+2*n):
            ans += 1
        else:
            uf.unite(x,y+n)
            uf.unite(x+n,y+2*n)
            uf.unite(x+2*n,y)

print(ans)
