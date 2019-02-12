# -*- coding: utf-8 -*-
import heapq
n,k = map(int, input().split())
ab = []
for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(ab, (a,b))


res = 0
for _ in range(k):
    a,b = heapq.heappop(ab)
    res += a
    a += b
    heapq.heappush(ab, (a,b))

print(res)
