# -*- coding: utf-8 -*-
from itertools import combinations

n,W = map(int, input().split())
vl = []
vmax = 0
wl = []
wmax = 0
for _ in range(n):
    v,w = map(int, input().split())
    vl.append(v)
    wl.append(w)
    vmax = max(vmax, v)
    wmax = max(wmax, w)


if n<=30:
    m = n//2
    l = []
    for r in range(m+1):
        for cl in combinations(range(m),r):
            v,w = 0,0
            for i in cl:
                v += vl[i]
                w += wl[i]
            if w<W:
                l.append((w,-v))
    l.sort()
    ll = []
    v,w = 0,0
    for i in range(len(l)):
        if w<l[i][0] and v<-l[i][1]:
            ll.append((l[i][0],-l[i][1]))
            w = l[i][0]
            v = -l[i][1]
    res = 0
    for r in range(n-m+1):
        for cl in combinations(range(m,n),r):
            v,w = 0,0
            for i in cl:
                v += vl[i]
                w += wl[i]
            ok = -1
            ng = len(ll)
            while ng-ok>1:
                mid = (ok+ng)//2
                if ll[mid][0]+w<=W:
                    ok = mid
                else:
                    ng = mid
            if ok>=0:
                res = max(res, v+ll[ok][1])
            elif w<=W:
                res = max(res,v)
    print(res)
elif vmax<=1000:
    inf = 10**15
    dp = [[inf]*(n*vmax+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n*vmax+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j-vl[i]>=0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-vl[i]]+wl[i])
    res = 0
    for i in range(n*vmax+1):
        if dp[n][i]<=W:
            res = max(res,i)
    print(res)
elif wmax<=1000:
    dp = [[0]*(n*wmax+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n*wmax+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j-wl[i]>=0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-wl[i]]+vl[i])
    print(max(dp[n][:W+1]))