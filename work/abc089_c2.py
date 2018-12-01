# -*- coding: utf-8 -*-
from itertools import combinations
n = int(input())
d = {
    "M": 0
    ,"A": 0
    ,"R": 0
    ,"C": 0
    ,"H": 0
}

for _ in range(n):
    s = input()
    if s[0] in d:
        d[s[0]] += 1

res = 0
for c in combinations(d.keys(), 3):
    res += d[c[0]]*d[c[1]]*d[c[2]]
print(res)
