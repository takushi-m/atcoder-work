# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

res = 0
for i in range(n):
    if al[i]<bl[i]:
        res += al[i]
        bl[i] -= al[i]
        al[i] = 0
    else:
        res += bl[i]
        al[i] -= bl[i]
        bl[i] = 0

    if bl[i]>0:
        if al[i+1]<bl[i]: 
            res += al[i+1]
            bl[i] -= al[i+1]
            al[i+1] = 0
        else:
            res += bl[i]
            al[i+1] -= bl[i]
            bl[i] = 0

print(res)