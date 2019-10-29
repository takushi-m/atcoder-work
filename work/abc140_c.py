# -*- coding: utf-8 -*-
n = int(input())
bl = list(map(int, input().split()))
al = [0]*n

al[0] = bl[0]
al[n-1] = bl[-1]
for i in range(1,n-1):
    al[i] = min(bl[i-1],bl[i])

print(sum(al))