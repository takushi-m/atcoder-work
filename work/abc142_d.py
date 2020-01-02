# -*- coding: utf-8 -*-
from math import sqrt
a,b = map(int, input().split())
xa,xb = a,b

sa = set([1])
i = 2
while a>1:
    if i>sqrt(xa):
        sa.add(a)
        break
    while a%i==0:
        sa.add(i)
        a //= i
    i += 1

sb = set([1])
i = 2
while b>1:
    if i>sqrt(xb):
        sb.add(b)
        break
    while b%i==0:
        sb.add(i)
        b //= i
    i += 1

print(len(sa & sb))