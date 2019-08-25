# -*- coding: utf-8 -*-
n,k = map(int, input().split())
al = list(map(int, input().split()))
MOD = 10**9+7

d = {}
for a in al:
    if a not in d:
        d[a] = 0
    d[a] += 1

res = 0
for i in range(n-1):
    for j in range(i+1,n):
        if al[i]>al[j]:
            res += 1
            res %= MOD
res = res*k
res %= MOD

for i in range(n):
    r = 0
    for key in d:
        if al[i]>key:
            r += d[key]
    res += r*k*(k-1)//2
    res %= MOD

print(res)
