# -*- coding: utf-8 -*-
from operator import itemgetter

n,m = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(m)], key=itemgetter(1))

res = 0
s = 0
for a,b in ab:
    if a<=s<b:
        continue
    s = b-1
    res += 1

print(res)
