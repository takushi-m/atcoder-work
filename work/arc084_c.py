# -*- coding: utf-8 -*-
import bisect

n = int(input())
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
c = sorted([int(x) for x in input().split()])

cnt = 0
for j in range(n):
    ai = bisect.bisect_left(a,b[j])
    ci = n-bisect.bisect_right(c,b[j])
    cnt += ai*ci
print(cnt)
