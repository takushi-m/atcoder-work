# -*- coding: utf-8 -*-
n,k = map(int, input().split())
pl = list(map(int, input().split()))

ppl = [0]*n
for i in range(n):
    ppl[i] = (pl[i]+1)/2

acc = [0]*(n+1)
for i in range(n):
    acc[i+1] += acc[i]+ppl[i]

res = -1
for i in range(n-k+1):
    res = max(res, acc[i+k]-acc[i])

print(res)