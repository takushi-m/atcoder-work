# -*- coding: utf-8 -*-
class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return

        if x<y:
            self.par[y] = x
        else:
            self.par[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


n,m = map(int, input().split())
uf = UnionFind(n+m)

for u in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    for l in line[1:]:
        lng = n+l-1
        uf.unite(u, lng)

flag = True
for u in range(1,n):
    if not uf.same(0,u):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
