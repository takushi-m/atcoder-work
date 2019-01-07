# -*- coding: utf-8 -*-
n = int(input())
hl = list(map(int, input().split()))

dp = [0]*n
dp[1] = abs(hl[1]-hl[0])

for i in range(2,n):
    dp[i] = min(
        dp[i-1] + abs(hl[i]-hl[i-1]),
        dp[i-2] + abs(hl[i]-hl[i-2])
    )

print(dp[n-1])
