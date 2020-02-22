# -*- coding: utf-8 -*-
n,k = map(int, input().split())
sl = [int(input()) for _ in range(n)]

if 0 in sl:
    print(n)
    exit()

res = 0
p = 1
r = 0
l = 0
while l<n:
    while r<n and p*sl[r]<=k:
        p *= sl[r]
        r += 1

    res = max(res, r-l)

    if r==l:
        r += 1
    else:
        p //= sl[l]

    l += 1

print(res)