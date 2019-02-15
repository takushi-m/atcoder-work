# -*- coding: utf-8 -*-
from math import sqrt
k = int(input())

def f1(c,r):
    res1 = 0
    for x in range(c,r+1,c):
        for y in range(c,r+1,c):
            if sqrt(x*x+y*y)<=r:
                res1 += 1
    return 4*res1

def f2(c,r):
    res1 = 0
    for xi in range(c,r+1,c):
        x = c/2+xi
        for yi in range(c,r+1,c):
            y = c/2+yi
            if sqrt(x*x+y*y)<=r:
                res1 += 1
    r1 = 0
    for yi in range(c,r+1,c):
        y = c/2+yi
        x = c/2
        if sqrt(x*x+y*y)<=r:
            r1 += 1
    return 4*res1 + 4*r1 + 1

# f1(k,150)
print(min(f1(k,100),f2(k,100)), min(f1(k,150),f2(k,150)))
