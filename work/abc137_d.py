# -*- coding: utf-8 -*-
import heapq

n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x:(x[0],-x[1]))
q = []

res = 0
idx = 0
for i in range(1,m+1):
    while idx<n and ab[idx][0]<=i:
        heapq.heappush(q,-ab[idx][1])
        idx += 1

    if len(q)>0:
        res += -q[0]
        heapq.heappop(q)

print(res)
