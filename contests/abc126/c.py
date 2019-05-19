# -*- coding: utf-8 -*-
n,k = map(int, input().split())

bp = []
for i in range(30):
    bp.append(1/2**i)

res = 0
for i in range(1,n+1):
    if i>=k:
        res += 1/n
        continue
    x = i
    cnt = 0
    while x<k:
        x *= 2
        cnt += 1
    res += bp[cnt]/n

print("{:.12f}".format(res))
