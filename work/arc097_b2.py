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
pl = list(map(int, input().split()))

u = UnionFind(n+1)
for _ in range(m):
  x,y = map(int, input().split())
  u.unite(x,y)

res = 0
for i in range(1,n+1):
  if u.same(i,pl[i-1]):
    res += 1
print(res)