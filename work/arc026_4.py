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
abct = [list(map(int, input().split())) for _ in range(m)]

def check(x):
    uf = UnionFind(n+1)
    l = [(abct[i][2]-abct[i][3]*x, abct[i][0], abct[i][1]) for i in range(m)]
    l.sort()
    rem = []
    s = 0
    for c,a,b in l:
        if uf.same(a,b):
            rem.append((c,a,b))
            continue
        s += c
        uf.unite(a,b)
    if s<=0:
        return True
    for c,a,b in rem:
        s += c
        if s<=0:
            return True
    return False

ng = 0
ok = 10**7
while ok-ng>10**-3:
    mid = (ok+ng)/2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)