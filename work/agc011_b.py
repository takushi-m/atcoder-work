# -*- coding: utf-8 -*-
n = int(input())
a = sorted([int(x) for x in input().split()])

s = 0
k = -1
for i in range(n-1):
    s += a[i]
    if 2*s<a[i+1]:
        k = i

if k==-1:
    print(n)
else:
    print(n-k-1)
