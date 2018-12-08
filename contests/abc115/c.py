# -*- coding: utf-8 -*-
n,k = map(int, input().split())
hl = []
for _ in range(n):
    hl.append(int(input()))
hl.sort()

res = 10**9
for i in range(n-k+1):
    hmin,hmax = hl[i],hl[i+k-1]
    res = min(res, hmax-hmin)

print(res)
