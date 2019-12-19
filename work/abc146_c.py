# -*- coding: utf-8 -*-
from math import log10
a,b,x = map(int, input().split())

def check(n):
    return a*n+b*len(str(n)) <= x


ok = 0
ng = 10**9 + 1
while abs(ng-ok)>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
