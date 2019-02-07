# -*- coding: utf-8 -*-
# セグメント木でRMQ
MAX_N = 2**30
INF = 10**9

class SegTree(object):
    """docstring for SegTree."""
    def __init__(self, l, n):
        self.dat = [INF for _ in range(MAX_N*2-1)]
        for i in range(n):
            self.dat[i+n-1] = l[i]
        self.init(0)

    def init(self, i):
        if i>n-1:
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
        i += n-1
        self.dat[i] = x
        while i>0:
            i = self.par(i)
            self.dat[i] = min(
                self.dat[self.left(i)],
                self.dat[self.right(i)]
            )

    def q(self,a,b):
