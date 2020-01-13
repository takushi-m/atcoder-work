# -*- coding: utf-8 -*-
from itertools import combinations

s = input()
n = len(s)

def gen():
    l = []
    for i in range(n):
        l.append(s[i])
        l.append("")
    return l

res = 0
for r in range(n):
    for p in combinations(range(n-1),r):
        e = gen()
        for i in p:
            e[2*i+1] = "+"
        res += eval("".join(e))

print(res)