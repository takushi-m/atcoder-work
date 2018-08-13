# -*- coding: utf-8 -*-

INF = 999999999
n = int(input())

coins = [1]

s = 9
while s<=n:
    coins.append(s)
    s *= 9

s = 6
while s<=n:
    coins.append(s)
    s *= 6

coins.sort(reverse=True)

dp = [INF for _ in range(n+1)]
dp[0] = 0

for i in range(1,n+1):
    for c in coins:
        if i-c>=0:
            dp[i] = min(dp[i], dp[i-c]+1)

print(dp[-1])
