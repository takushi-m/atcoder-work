# -*- coding: utf-8 -*-
from itertools import combinations
s = input()

ret = 0
for i in range(len(s)):
    for c in combinations(range(1, len(s)), i):
        e = s
        for idx,j in enumerate(c):
            e = e[:idx+j]+"+"+e[idx+j:]
        exec("ret+="+e)
print(ret)
