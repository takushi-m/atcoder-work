# -*- coding: utf-8 -*-
from itertools import permutations
from math import sqrt
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

def d(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    

res = 0.0
cnt = 0
for p in permutations(range(n), n):
    cnt += 1
    for i in range(n-1):
        res += d(xy[p[i]],xy[p[i+1]])

print(res/cnt)