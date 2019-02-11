# -*- coding: utf-8 -*-
from math import log10, ceil
n,m = map(int, input().split())
rl = list(map(int, input().split()))

logfac = [0]
for i in range(1,10**5+10):
    logfac.append(logfac[i-1] + log10(i))

def logcomb(x,y):
    res1 = logfac[x] # sum([log10(i) for i in range(1,x+1)])
    res2 = logfac[x-y] # sum([log10(i) for i in range(1,x-y+1)])
    res3 = logfac[y] # sum([log10(i) for i in range(1,y+1)])
    return res1-res2-res3

rs = 0
s = 0
for i in range(m):
    s += logcomb(n-rs, rl[i])
    rs += rl[i]

print(ceil(-1.0*(s-n*log10(m))))
