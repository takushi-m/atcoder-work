# -*- coding: utf-8 -*-
from itertools import product
s = list(input())
n = len(s)
x = []
for i in range(n-1):
    x.append(s[i])
    x.append("")
x.append(s[n-1])

res = 0
for l in product(["","+"],repeat=n-1):
    for i in range(n-1):
        x[2*i+1] = l[i]
    res += eval("".join(x))
print(res)
