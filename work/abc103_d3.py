# -*- coding: utf-8 -*-
from operator import itemgetter
n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

res = 0
ab.sort(key=itemgetter(1))

i = 0
while i<m:
    a,b = ab[i]
    for j in range(i+1,m):
        if ab[j][0]<b<=ab[j][1]:
            i += 1
        else:
            break
    i += 1
    res += 1

print(res)
