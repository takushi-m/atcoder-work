# -*- coding: utf-8 -*-
import heapq
n,m = map(int, input().split())
q = []
s = 0
for a in input().split():
    a = int(a)
    s += a
    q.append(-a)

heapq.heapify(q)

for _ in range(m):
    x = q[0]
    heapq.heappop(q)
    heapq.heappush(q,-1*((-x)//2))

print(-1*sum(q))
