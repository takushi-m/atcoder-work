# -*- coding: utf-8 -*-
from itertools import combinations
n = int(input())

primes = []
for i in range(1,n+1):
    z = 2
    while z<=i:
        while i%z==0:
            i //= z
            primes.append(z)
        z += 1

d = {}
for x in primes:
    if x not in d:
        d[x] = 0
    d[x] += 1

keys = list(d.keys())
res = 0

for k in keys:
    if d[k]>=74:
        res += 1
if len(keys)>=2:
    for c in combinations(keys,2):
        if d[c[0]]>=24 and d[c[1]]>=2:
            res += 1
        if d[c[0]]>=2 and d[c[1]]>=24:
            res += 1

        if d[c[0]]>=4 and d[c[1]]>=14:
            res += 1
        if d[c[0]]>=14 and d[c[1]]>=4:
            res += 1
if len(keys)>=3:
    for c in combinations(keys, 3):
        if d[c[0]]>=4 and d[c[1]]>=4 and d[c[2]]>=2:
            res += 1
        if d[c[0]]>=4 and d[c[1]]>=2 and d[c[2]]>=4:
            res += 1
        if d[c[0]]>=2 and d[c[1]]>=4 and d[c[2]]>=4:
            res += 1
print(res)
