# -*- coding: utf-8 -*-
n,ma,mb = map(int, input().split())
abc = []
sa = 0
sb = 0
for _ in range(n):
    a,b,c = map(int, input().split())
    sa += a
    sb += b
    abc.append((a,b,c))
inf = 10**5
dp = [[[inf for _ in range(sb+1)] for _ in range(sa+1)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    a,b,c = abc[i]
    for ai in range(sa+1):
        for bi in range(sb+1):
            dp[i+1][ai][bi] = min(dp[i+1][ai][bi], dp[i][ai][bi])
            if ai+a<sa+1 and bi+b<sb+1:
                dp[i+1][ai+a][bi+b] = min(dp[i+1][ai+a][bi+b], dp[i][ai][bi]+c)
# print(dp)

res = inf
for ai in range(1,sa+1):
    for bi in range(1,sb+1):
        if ma*bi==mb*ai:
            res = min(res, dp[n][ai][bi])
if res == inf:
    print(-1)
else:
    print(res)
