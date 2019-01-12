# -*- coding: utf-8 -*-
h,w = map(int, input().split())
al = [input() for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]
MOD = 10**9 + 7
dp[0][0] = 1
for hi in range(h):
    for wi in range(w):
        if al[hi][wi]=="#":
            continue
        s = 0
        if hi-1>=0:
            s += dp[hi-1][wi]
        if wi-1>=0:
            s += dp[hi][wi-1]
        dp[hi][wi] += s
        dp[hi][wi] %= MOD

print(dp[h-1][w-1])
