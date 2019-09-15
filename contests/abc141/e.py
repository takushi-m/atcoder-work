# -*- coding: utf-8 -*-
n = int(input())
s = input()

d = {}
res = 0
for l1 in range(n):
    for l2 in range(l1+1,n+1):
        ss = s[l1:l2]
        if ss not in d:
            d[ss] = l1
        else:
            if d[ss]+len(ss)<=l1:
                res = max(res,len(ss))
print(res)
