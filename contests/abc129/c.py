# -*- coding: utf-8 -*-
n,m = map(int, input().split())
a = set([int(input()) for _ in range(m)])
MOD = 1000000007

dp = [0]*(n+2)
dp[0] = 1
for i in range(n):
    if i+1 not in a:
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
    if i+2 not in a:
        dp[i+2] += dp[i]
        dp[i+2] %= MOD

print(dp[n])
