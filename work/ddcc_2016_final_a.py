# -*- coding: utf-8 -*-
from math import sqrt
r,c = map(int, input().split())
res = 0

def check(x,y):
    return sqrt(x*x+y*y)<=r

for x in range(c,r+1,c):
    for y in range(c,r+1,c):
        if check(x,y):
            res += 1

print(4*res)
