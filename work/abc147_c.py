# -*- coding: utf-8 -*-
from itertools import combinations

n = int(input())

al = []
for _ in range(n):
    a = int(input())
    xy = [list(map(int, input().split())) for _ in range(a)]
    al.append(xy)

res = 0
for i in range(1,n+1):
    for c in combinations(range(n), i):
        flag = True
        for X in c:
            for x,y in al[X]:
                if y==1:
                    if x-1 not in c:
                        flag = False
                else:
                    if x-1 in c:
                        flag = False
        if flag:
            res = i
            break

print(res)
