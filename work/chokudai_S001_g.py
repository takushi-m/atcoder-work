# -*- coding: utf-8 -*-
from math import log10,ceil
n = int(input())
al = list(map(int, input().split()))
MOD = 10**9+7

al = reversed(al)

b = 1
res = 0
for a in al:
    res += a*b
    res %= MOD

    b *= 10**ceil(log10(a+1))
    b %= MOD

print(res)