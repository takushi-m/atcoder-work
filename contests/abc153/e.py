# -*- coding: utf-8 -*-
h,n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

inf = 10**9
dp = [inf]*(h+1)
dp[0] = 0
for i in range(n):
    for j in range(h+1):
        d = min(j+ab[i][0], h)
        dp[d] = min(dp[d], dp[j]+ab[i][1])

res = dp[h]
print(res)
