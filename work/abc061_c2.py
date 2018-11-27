# -*- coding: utf-8 -*-
n,k = map(int, input().split())
ab = []
for _ in range(n):
    a,b = map(int, input().split())
    ab.append((a,b))

ab.sort()

res = 0
for a,b in ab:
    if b>=k:
        res = a
        break
    else:
        k -= b
print(res)
