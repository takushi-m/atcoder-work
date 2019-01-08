# -*- coding: utf-8 -*-
N,W = map(int, input().split())
wl = []
vl = []
for _ in range(N):
    w,v = map(int, input().split())
    wl.append(w)
    vl.append(v)

INF = 10**11
V = sum(vl)+1
dp = [[INF for _ in range(V+1)] for _ in range(N+1)]
dp[0][0] = 0

for vi in range(V+1):
    for i in range(N):
        if vi>=vl[i]:
            dp[i+1][vi] = min(
                dp[i][vi],
                dp[i][vi-vl[i]]+wl[i]
            )
        else:
            dp[i+1][vi] = dp[i][vi]

res = 0
for vi in range(V+1):
    if dp[N][vi]<=W:
        res = max(res, vi)

print(res)
