# -*- coding: utf-8 -*-
n = int(input())
d = {}

for _ in range(n):
    s = "".join(sorted(list(input())))
    if s not in d:
        d[s] = 0
    d[s] += 1

res = 0
for k in d:
    n = d[k]
    res += n*(n-1)//2

print(res)
