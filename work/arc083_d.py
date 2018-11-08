# -*- coding: utf-8 -*-
n = int(input())
d = []
for i in range(n):
    line = [int(x) for x in input().split()]
    d.append(line)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j]>d[i][k]+d[k][j]:
                print(-1)
                exit()

res = 0
for i in range(i):
    for j in range(i+1,n):
        flag = True
        for k in range(n):
            if i==k or j==k:
                continue
            if d[i][j]==d[i][k]+d[k][j]:
                flag = False
                break
        if flag:
            res += d[i][j]
print(res)
