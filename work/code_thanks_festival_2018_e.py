# -*- coding: utf-8 -*-
t = int(input())
al = list(map(int, input().split()))
MOD = 10**9+7

dp = [[0]*601 for _ in range(t+1)]
dp[0][0] = 1

for i in range(t):
    for j in range(300+1):
        for k in range(al[i]+1):
            dp[i+1][j+k] += dp[i][j*2]
            dp[i+1][j+k] %= MOD
res = 0
for i in range(t+1):
    res += dp[i][1]
    res %= MOD
idx = 2
while idx<=601:
    res += dp[t][idx]
    res %= MOD
    idx *= 2
print(res)
