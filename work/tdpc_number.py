# -*- coding: utf-8 -*-
MOD = 10**9 + 7
d = int(input())
ns = input()
n = len(ns)

dp = [[[0]*d for _ in [0,1]] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n):
    c = int(ns[i])
    for j in [0,1]:
        for k in range(d):
            m = 9 if j==1 else c
            for digit in range(m+1):
                f = 1 if (j==1 or digit<c) else 0
                dp[i+1][f][(k+digit)%d] += dp[i][j][k]
                dp[i+1][f][(k+digit)%d] %= MOD

print((dp[n][0][0]+dp[n][1][0])%MOD - 1)