# -*- coding: utf-8 -*-
c,d = map(int, input().split())
l = 140
r = 170

def f(l,r):
    if r<=c:
        return 0
    if d<=l:
        return 0
    if c<=l and r<=d:
        return r-l
    if l<=c and d<=r:
        return d-c
    if r<d:
        return r-c
    return d-l

res = 0
while l<d:
    res += f(l,r)
    l *= 2
    r *= 2

print(res)
