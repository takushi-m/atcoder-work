# -*- coding: utf-8 -*-
n = int(input())

al = []
i = 1
for a in input().split():
    a = int(a)
    al.append((a,i))
    i += 1
al = sorted(al)
print(" ".join([str(al[i][1]) for i in range(n)]))