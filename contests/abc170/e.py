# セグメント木
class SegTree:
    """docstring for SegTree."""
    def __init__(self, l, _n, u, f):
        n = 1
        while n<_n:
            n *= 2
        self.n = n
        self.dat = [u for _ in range(2*n)]
        self.u = u
        self.f = f
        for i in range(_n):
            self.dat[i+n-1] = l[i]
        self.init(0)

    def init(self, i):
        if i>=self.n-1:
            return self.dat[i]
        self.dat[i] = self.f(
            self.init(self.left(i)),
            self.init(self.right(i))
        )
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
            self.dat[i] = self.f(
                self.dat[self.left(i)],
                self.dat[self.right(i)]
            )

    def q(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.u[0]
        if a<=l and r<=b:
            return self.dat[k][0]
        return min(
            self.q(a,b,self.left(k),l,(l+r)//2),
            self.q(a,b,self.right(k),(l+r)//2,r)
        )

    def query(self,a,b):
        return self.q(a,b,0,0,self.n)


def f(l,r):
    if l[1]!=r[1]:
        if l[0]<r[0]:
            return l
        else:
            return r
    if l[0]>r[0]:
        return l
    else:
        return r

n,q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]


seg = SegTree(l,n,[10**9+1,-1],f)
res = []
for _ in range(q):
    c,d = map(int, input().split())
    seg.update(c-1, [seg.dat[c-1][0], d])
    res.append(seg.query(0,n))
for r in res:
    print(r)
