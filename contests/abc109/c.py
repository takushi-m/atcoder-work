# -*- coding: utf-8 -*-
from fractions import gcd
n,x = map(int, input().split())
ary = [abs(x-int(i)) for i in input().split()]

d = ary[0]
for i in ary[1:]:
    d = gcd(i,d)

print(d)
