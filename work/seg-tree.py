# -*- coding: utf-8 -*-
# セグメント木でRMQ
INF = 10**9

class SegTree(object):
    """docstring for SegTree."""
    def __init__(self, l, _n):
        n = 1
        while n<_n:
            n *= 2
        self.n = n
        self.dat = [INF for _ in range(2*n)]
        for i in range(_n):
            self.dat[i+n-1] = l[i]
        self.init(0)

    def init(self, i):
        if i>=self.n-1:
            return self.dat[i]
        self.dat[i] = min(
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
            self.dat[i] = min(
                self.dat[self.left(i)],
                self.dat[self.right(i)]
            )

    def q(self,a,b,k,l,r):
        if r<=a or b<=l:
            return INF
        if a<=l and r<=b:
            return self.dat[k]
        return min(
            self.q(a,b,self.left(k),l,(l+r)//2),
            self.q(a,b,self.right(k),(l+r)//2,r)
        )

    def query(self,a,b):
        return self.q(a,b,0,0,self.n)

def f(l,a,b):
    res = INF
    for i in range(a,b):
        res = min(res, l[i])
    return res

if __name__ == '__main__':
    from random import randint
    n = 1000
    l = [randint(0,100) for _ in range(n)]
    seg =SegTree(l, n)

    q = [
        (0,n),
        (10,11),
        (n-10,n-5),
        (100,200)
    ]
    for a,b in q:
        print(f(l,a,b), seg.query(a,b))

    l[10] = 0
    seg.update(10,0)
    print(f(l,10,11),seg.query(10,11))
