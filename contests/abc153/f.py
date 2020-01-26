# -*- coding: utf-8 -*-
import heapq
from math import ceil
n,d,a = map(int, input().split())
xh = [list(map(int, input().split())) for _ in range(n)]
xh.sort()

res = 0
b = []
heapq.heapify(b)
r = 0
for i in range(n):
    x,h = xh[i]

    while len(b)>0 and b[0][0]<=x:
        r += b[0][1]
        heapq.heappop(b)
    c = max(ceil((h-r)/a), 0)
    res += c
    r += c*a
    
    if c>0:
        heapq.heappush(b, (x+2*d+1, -c*a))

print(res)