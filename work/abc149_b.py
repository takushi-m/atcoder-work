# -*- coding: utf-8 -*-
a,b,k = map(int, input().split())

if a<k:
    k -= a
    a = 0
    b = max(0, b-k)
else:
    a -= k

print(a,b)