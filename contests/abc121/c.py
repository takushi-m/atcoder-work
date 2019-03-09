# -*- coding: utf-8 -*-
n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

res = 0
for i in range(n):
    if m>=ab[i][1]:
        res += ab[i][0]*ab[i][1]
        m -= ab[i][1]
    else:
        res += ab[i][0]*m
        m = 0

    if m==0:
        break

print(res)
