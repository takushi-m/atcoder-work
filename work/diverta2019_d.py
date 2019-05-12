# -*- coding: utf-8 -*-
from math import sqrt
n = int(input())

selected = set()
res = 0
for w in range(1,int(sqrt(n))+10):
    if n%w==0:
        m = (n-w)//w
        if m>0 and m not in selected and n//m == n%m:
            res += m
            selected.add(m)

        w2 = n//w
        m2 = (n-w2)//w2
        if m2>0 and m2 not in selected and n//m2 == n%m2:
            res += m2
            selected.add(m2)
print(res)
