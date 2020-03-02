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

n,m,k = map(int, input().split())
uf = UnionFind(n+1)
dd = {}
for i in range(n):
    dd[i] = set()

for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    dd[a].add(b)
    dd[b].add(a)
    uf.unite(a,b)

for _ in range(k):
    c,d = map(int, input().split())
    c -= 1
    d -= 1
    if not uf.same(c,d):
        continue
    dd[c].add(d)
    dd[d].add(c)

res = [0]*n
for i in range(n):
    res[i] = uf.size(i) - len(dd[i]) - 1

print(*res)