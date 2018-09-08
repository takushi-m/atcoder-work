# -*- coding: utf-8 -*-
from statistics import mean
from math import factorial as fact

n,a,b = map(int, input().split())
v = sorted([int(x) for x in input().split()], reverse=True)
sel = v[:a]
print(mean(sel))

vn = v.count(sel[-1])
na = sel.count(sel[-1])
nb = min(b-a, vn-na)
# print(na,nb,vn,len(sel),sel[-1])

if na!=len(sel):
    print(fact(vn)//(fact(na)*fact(vn-na)))
elif nb==0:
    print(1)
else:
    ret = 0
    for bi in range(na,na+nb+1):
        ret += fact(vn)//(fact(bi)*fact(vn-bi))
    print(ret)
