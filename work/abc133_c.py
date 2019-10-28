# -*- coding: utf-8 -*-
l,r = map(int, input().split())

if r-l+1>=2019 or l==0:
    print(0)
else:
    res = 2019*2019
    for i in range(l,r):
        for j in range(i+1,r+1):
            res = min(res, (i*j)%2019)
    print(res)