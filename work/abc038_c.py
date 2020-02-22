# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

res = 0
l = 0
r = 0
last = -1
while l<n:
    while r<n and last<al[r]:
        last = al[r]
        r += 1
    while l<r:
        res += r-l-1
        l += 1
    r += 1
    if l<n:
        last = al[l]

print(res+n)