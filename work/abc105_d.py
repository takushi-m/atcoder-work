# -*- coding: utf-8 -*-
n,m = map(int, input().split())
bmap = {0: 1}
ret = 0
b = 0
for a in list(map(int, input().split())):
    b += a
    r = b%m
    if r not in bmap:
        bmap[r] = 0
    bmap[r] += 1


for r in bmap.values():
    ret += r*(r-1)//2
print(ret)
