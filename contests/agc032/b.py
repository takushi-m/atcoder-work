# -*- coding: utf-8 -*-
from itertools import permutations

n = int(input())
res = []
for r in permutations(range(1,n+1)):
    c = r[0]+r[2]
    flag = True
    for i in range(1,n-1):
        if r[i-1]+r[i+1]!=c:
            flag = False
            break
    if r[1]==r[n-2]==c:
        pass
    elif r[1]+r[n-1]==c:
        res.append((r[1],r[n-1]))
    else:
        flag = False

    if flag:
        for i in range(n-1):
            res.append((r[i],r[i+1]))
        break

print(len(res))
for r in res:
    print(r[0],r[1])
