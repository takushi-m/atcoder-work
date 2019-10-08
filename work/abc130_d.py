# -*- coding: utf-8 -*-
n,k = map(int, input().split())
al = list(map(int, input().split())) + [0]

cnt = 0
r = 0
s = 0
for l in range(n):
    while r<n and s<k:
        s += al[r]
        r += 1

    if s<k:
        break
    cnt += n-r+1

    if r==l:
        r += 1
    else:
        s -= al[l]

print(cnt)
