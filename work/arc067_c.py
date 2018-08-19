# -*- coding: utf-8 -*-
n = int(input())
MOD = 10**9 + 7

d = {}
for i in range(2,n+1):
    for j in range(2,i+1):
        while i%j==0:
            if j not in d:
                d[j] = 1
            d[j] += 1
            i = i//j
ret = 1
for v in d.values():
    ret = (ret*v)%MOD
print(ret)
