# -*- coding: utf-8 -*-
n = int(input())
pl = list(map(int, input().split()))
p = sum(pl)

dp = [[0]*(p+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(p+1):
        dp[i+1][j] = dp[i][j]
        if j-pl[i]>=0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-pl[i]])

print(sum(dp[n]))