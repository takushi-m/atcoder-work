# -*- coding: utf-8 -*-
n = int(input())
vl = list(map(int, input().split()))
vl = sorted(vl)

r = vl[0]
for i in range(1,n):
    y = vl[i]
    r = (r+y)/2
print(r)
