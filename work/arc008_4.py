def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a>=key

    ng = -1
    ok = len(al)

    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid

    return ok

class SegTree(object):
    """docstring for SegTree."""
    def __init__(self, l, _n, u, f):
        n = 1
        while n<_n:
            n *= 2
        self.n = n
        self.dat = [u for _ in range(2*n)]
        self.f = f
        self.u = u
        for i in range(_n):
            self.dat[i+n-1] = l[i]
        self.init(0)

    def init(self, i):
        if i>=self.n-1:
            return self.dat[i]
        self.dat[i] = self.f(self.init(self.left(i)), self.init(self.right(i)))
        return self.dat[i]

    def par(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def update(self, i, x):
        i += self.n-1
        self.dat[i] = x
        while i>0:
            i = self.par(i)
            self.dat[i] = self.f(self.dat[self.left(i)], self.dat[self.right(i)])

    def q(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.u
        if a<=l and r<=b:
            return self.dat[k]

        return self.f(self.q(a,b,self.left(k),l,(l+r)//2), self.q(a,b,self.right(k),(l+r)//2,r))

    def query(self,a,b):
        return self.q(a,b,0,0,self.n)


n,m = map(int, input().split())
u = (1,0)
seg = SegTree(
    [u for _ in range(m)],
    m,
    u,
    lambda l,r: (l[0]*r[0], r[0]*l[1]+r[1])
)

lq = []
l = []
for _ in range(m):
    q,a,b = input().split()
    q = int(q)-1
    a = float(a)
    b = float(b)
    lq.append(q)
    l.append((q,a,b))
lq.sort()

rmin = 1
rmax = 1
for q,a,b in l:
    idx = lower_bound(lq, q)
    seg.update(idx, (a,b))
    x,y = seg.query(0,m)
    rmin = min(rmin, x+y)
    rmax = max(rmax, x+y)
print(rmin)
print(rmax)