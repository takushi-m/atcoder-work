# -*- coding: utf-8 -*-
n = int(input())
vl = list(map(int, input().split()))
cl = list(map(int, input().split()))

res = -1

for i in range(2**n):
    x = 0
    y = 0
    for j in range(n):
        if i>>j&1==1:
            x += vl[j]
            y += cl[j]
    res = max(res, x-y)

print(res)
