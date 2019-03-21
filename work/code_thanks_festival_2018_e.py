# -*- coding: utf-8 -*-
t = int(input())
al = list(map(int, input().split()))
MOD = 10**9+7
ma = max(al)
dp = [[0]*(2*ma+1) for _ in range(t+1)]
dp[0][0] = 1

for i in range(t):
    for j in range(ma+1):
        for k in range(al[i]+1):
            dp[i+1][j+k] += dp[i][j*2]
            dp[i+1][j+k] %= MOD
res = 0
for i in range(t+1):
    res += dp[i][1]
    res %= MOD
idx = 2
while idx<=2*ma+1:
    res += dp[t][idx]
    res %= MOD
    idx *= 2
print(res)
