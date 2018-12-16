# -*- coding: utf-8 -*-
import math
n,h = map(int, input().split())
al = []
bl = []
for i in range(n):
    a,b = map(int, input().split())
    al.append(a)
    bl.append(b)
max_a = max(al)

bbl = []
for i in range(n):
    if bl[i]>max_a:
        bbl.append(bl[i])
bbl.sort(reverse=True)

res = 0
for b in bbl:
    h -= b
    res += 1
    if h<=0:
        break

if h>0:
    print(res+math.ceil(h/max_a))
else:
    print(res)
