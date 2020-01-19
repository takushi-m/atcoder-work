# -*- coding: utf-8 -*-
n = int(input())

c = [[0]*10 for _ in range(10)]

for i in range(1,n+1):
    sn = str(i)
    for ci in range(10):
        for cj in range(10):
            if sn[0]==str(ci) and sn[-1]==str(cj):
                c[ci][cj] += 1

res = 0
for i in range(10):
    for j in range(10):
        res += c[i][j]*c[j][i]
print(res)