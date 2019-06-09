# -*- coding: utf-8 -*-
n = int(input())
wl = list(map(int, input().split()))

res = 10**5
for i in range(n):
    s1 = sum(wl[0:i])
    s2 = sum(wl[i:])
    res = min(res, abs(s1-s2))

print(res)
