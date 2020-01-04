# -*- coding: utf-8 -*-
MOD = 10**9 + 7
n = int(input())
al = list(map(int, input().split()))

b = [0]*100

for a in al:
    for i in range(100):
        b[i] += (a>>i)&1

res = 0
for i in range(100):
    res += b[i]*(n-b[i])*(1<<i)
    res %= MOD

print(res)