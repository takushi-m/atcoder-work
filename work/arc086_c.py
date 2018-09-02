# -*- coding: utf-8 -*-
n,k = [int(x) for x in input().split()]

d = {}
for x in input().split():
    x = int(x)
    if x not in d:
        d[x] = 0
    d[x] += 1

cnt = 0
ret = 0
for kk,v in sorted(d.items(), key=lambda x:-x[1]):
    cnt += 1
    if cnt>k:
        ret += v
print(ret)
