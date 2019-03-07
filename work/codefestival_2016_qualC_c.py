# -*- coding: utf-8 -*-
n = int(input())
tl = list(map(int, input().split()))
al = list(map(int, input().split()))

mod = 10**9 + 7

res = 1
for i in range(1,n-1):
    if tl[i-1]<tl[i]:
        if tl[i]>al[i]:
            res = 0
        continue
    elif al[i]>al[i+1]:
        if al[i]>tl[i]:
            res = 0
        continue
    else:
        res *= min(al[i],tl[i])
        res %= mod
if tl[-1]!=al[0]:
    res = 0
print(res)
