# -*- coding: utf-8 -*-
w = int(input())
n,k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*(w+1) for _ in range(k+1)] for _ in range(n+1)]
for ni in range(1,n+1):
    for ki in range(1,k+1):
        for wi in range(1,w+1):
            dp[ni][ki][wi] = max(dp[ni][ki][wi], dp[ni-1][ki][wi])
            if wi-ab[ni-1][0]>=0:
                dp[ni][ki][wi] = max(dp[ni][ki][wi], dp[ni-1][ki-1][wi-ab[ni-1][0]]+ab[ni-1][1])

res = 0
for ki in range(k+1):
    res = max(res, dp[n][ki][w])
print(res)