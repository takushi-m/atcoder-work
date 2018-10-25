# -*- coding: utf-8 -*-
import bisect

n = int(input())
m = [-1 for _ in range(n)]
i = 0
for x in input().split():
    x = int(x)-1
    m[x] = i
    i += 1
d = [-1, n]
ans = 0
for i in range(n):
    idx = bisect.bisect(d,m[i])
    lo = m[i] - d[idx-1]
    hi = d[idx] - m[i]
    bisect.insort(d,m[i])
    ans += (i+1)*lo*hi
print(ans)
