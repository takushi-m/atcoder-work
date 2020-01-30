# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(input())
sd = defaultdict(int)
for _ in range(n):
    s = input()
    sd[s] += 1

m = int(input())
td = defaultdict(int)
for _ in range(m):
    t = input()
    td[t] += 1

res = 0
for s in sd:
    res = max(res, sd[s] - td[s])
print(res)