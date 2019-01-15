# -*- coding: utf-8 -*-
n,m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort(reverse=True)
al.append(0)
bl.sort(reverse=True)
bl.append(0)

res = 1
MOD = 10**9+7
ba = 0
bb = 0
for x in range(n*m,0,-1):
    if al[ba]>x or bl[bb]>x:
        res = 0
        break

    s = 1
    if al[ba]==x and bl[bb]==x:
        ba += 1
        bb += 1
    elif al[ba]==x:
        s = bb
        ba += 1
    elif bl[bb]==x:
        s = ba
        bb += 1
    else:
        s = ba*bb - (n*m-x)
    # print(x,ba,bb,s)
    if s<=0:
        res = 0
        break

    res = (res*s)%MOD

print(res)
