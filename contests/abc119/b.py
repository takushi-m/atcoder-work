# -*- coding: utf-8 -*-
from decimal import *
n = int(input())

res1 = Decimal(0)
res2 = Decimal(0)
for _ in range(n):
    x,u = input().split()
    if u=="JPY":
        res1 += Decimal(x)
    else:
        res2 += Decimal(x)*Decimal(380000.0)

print(res1+res2)
