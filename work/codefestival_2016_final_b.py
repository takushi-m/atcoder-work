# -*- coding: utf-8 -*-
n = int(input())

for k in range(1,n+1):
    s = k*(k+1)//2
    if s==n:
        res = set(range(1,k+1))
        break
    if s>=n and (s-n)<=k:
        res = set(range(1,k+1))
        res.remove(s-n)
        break

for r in res:
    print(r)
