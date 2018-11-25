# -*- coding: utf-8 -*-
n,m = map(int, input().split())

maxg = m//n+1

for x in range(maxg,0,-1):
    if (m - x*(n-1))%x==0:
        print(x)
        exit()
