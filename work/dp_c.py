# -*- coding: utf-8 -*-
n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]

for i in range(n):
    dp[i+1][0] = max(dp[i][1], dp[i][2]) + abc[i][0]
    dp[i+1][1] = max(dp[i][0], dp[i][2]) + abc[i][1]
    dp[i+1][2] = max(dp[i][0], dp[i][1]) + abc[i][2]

print(max(dp[n]))
