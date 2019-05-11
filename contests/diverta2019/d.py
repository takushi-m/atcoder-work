# -*- coding: utf-8 -*-
from math import sqrt
from itertools import product

n = int(input())
nn = n
d = {}
for i in range(2,int(sqrt(nn))+2):
    if n%i==0:
        while nn%i==0:
            nn //= i
            if i not in d:
                d[i] = []
            d[i].append(i)
if nn>1:
    d[nn] = [nn]

l = [d[k] for k in d.keys()]

def dfs(i, w):
    if i>=len(l):
        if n//w>int(sqrt(n)):
            return n//w-1
        return 0
    res = 0
    for x in range(len(l[i])+1):
        res += dfs(i+1, l[i][0]**x * w)
    return res
print(dfs(0,1))
