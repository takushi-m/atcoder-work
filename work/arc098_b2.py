# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

s = 0
res = 0
l = r = 0
while l<n:
    while r<n and s^al[r]==s+al[r]:
        s += al[r]
        r += 1

    res += r-l

    if r==l:
        r += 1
    else:
        s -= al[l]

    l += 1

print(res)