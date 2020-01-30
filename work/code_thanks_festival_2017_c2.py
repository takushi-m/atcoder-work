# -*- coding: utf-8 -*-
import heapq

n,k = map(int, input().split())
q = []
heapq.heapify(q)
for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(q, (a,b))

res = 0
for _ in range(k):
    a,b = heapq.heappop(q)
    res += a
    heapq.heappush(q, (a+b,b))

print(res)