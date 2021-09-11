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
        if c<0:
            res.append((v,u,c))
            cost += c
            uf.unite(v,u)
            continue

        if uf.same(v,u):
            continue
        res.append((v,u,c))
        cost += c
        uf.unite(v,u)
    return res,cost

n,m = map(int, input().split())
g = [[] for _ in range(n)]
cs = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b,c))
    # g[b].append((a,c))
    cs += c

_,c = kruskal(g,n)
print(cs-c)