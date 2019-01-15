# -*- coding: utf-8 -*-
from operator import itemgetter
n,d = map(int, input().split())
al = list(map(int, input().split()))
edge = []

def rec(left, right):
    if abs(right-left)<=1:
        return

    mid = (left+right)//2

    leftmin = left
    for i in range(left,mid):
        t = al[i] - d*i
        t2 = al[leftmin] - d*leftmin
        if t<t2:
            leftmin = i

    rightmin = mid
    for i in range(mid,right):
        t = al[i] + d*i
        t2 = al[rightmin] + d*rightmin
        if t2<t:
            rightmin = i

    for i in range(left,mid):
        edge.append((al[rightmin]+al[i]+abs(rightmin-i)*d, (i,rightmin)))
    for i in range(mid,right):
        edge.append((al[i]+al[leftmin]+abs(i-leftmin)*d, (leftmin,i)))

    rec(left,mid)
    rec(mid,right)

rec(0,n)

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

uf = UnionFind(n)
edge.sort(key=itemgetter(0))
res = 0
for e in edge:
    w = e[0]
    v,u = e[1]

    if uf.same(u,v):
        continue
    print(e)
    res += w
    uf.unite(v,u)

print(res)
