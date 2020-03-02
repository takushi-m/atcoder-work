
class SegTree(object):
    """docstring for SegTree."""
    def __init__(self, l, _n):
        n = 1
        while n<_n:
            n *= 2
        self.n = n
        self.dat = [0 for _ in range(2*n)]
        for i in range(_n):
            self.dat[i+n-1] |= 1<<l[i]
        self.init(0)

    def init(self, i):
        if i>=self.n-1:
            return self.dat[i]
        self.dat[i] = self.init(self.left(i)) | self.init(self.right(i))
        return self.dat[i]

    def par(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def update(self, i, x):
        i += self.n-1
        self.dat[i] = 1<<x
        while i>0:
            i = self.par(i)
            self.dat[i] = self.dat[self.left(i)] | self.dat[self.right(i)]

    def q(self,a,b,k,l,r):
        if r<=a or b<=l:
            return 0
        if a<=l and r<=b:
            return self.dat[k]
        return self.q(a,b,self.left(k),l,(l+r)//2) | self.q(a,b,self.right(k),(l+r)//2,r)

    def query(self,a,b):
        return self.q(a,b,0,0,self.n)

n = int(input())
s = [ord(c)-ord("a") for c in input()]
q = int(input())
ql = [input().split() for _ in range(q)]

seg = SegTree(s,n)

for i in range(q):
    if ql[i][0]=="1":
        seg.update(int(ql[i][1])-1, ord(ql[i][2])-ord("a"))
    else:
        r = seg.query(int(ql[i][1])-1, int(ql[i][2]))
        print(bin(r).count("1"))