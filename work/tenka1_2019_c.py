# -*- coding: utf-8 -*-

n = int(input())
s = input()

acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = acc[i]
    if s[i]==".":
        acc[i+1] += 1

res = 10**6
for i in range(n+1):
    r = acc[n] - acc[i]
    r += i - acc[i]
    res = min(res, r)

print(res)
