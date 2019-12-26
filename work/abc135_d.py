# -*- coding: utf-8 -*-
MOD = 10**9+7
s = input()
n = len(s)

dp = [[0]*13 for _ in range(n+1)]
dp[0][0] = 1
b = 1
for i in range(1,n+1):
    if s[n-i] == "?":
        for j in range(10):
            for k in range(13):
                dp[i][(j*b+k)%13] += dp[i-1][k]
    else:
        j = int(s[n-i])
        for k in range(13):
            dp[i][(j*b+k)%13] += dp[i-1][k]
    for k in range(13):
        dp[i][k] %= MOD
    b *= 10
    b %= 13

print(dp[n][5]%MOD)