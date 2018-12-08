# -*- coding: utf-8 -*-
n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
p.sort()

print(sum(p)-(p[n-1]//2))
