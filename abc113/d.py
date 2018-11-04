# -*- coding: utf-8 -*-
h,w,k = map(int, input().split())
mod = 1000000007

cnt = {
    -2: 0
    ,-1: 0
    ,0: 0
    ,1: 2
    ,2: 3
    ,3: 5
    ,4: 8
    ,5: 13
    ,6: 21
    ,7: 33
    ,8: 54
}

dp = [[0 for _ in range(w)] for _ in range(h+1)]
dp[0][0] = 1

for hi in range(1,h+1):
    for wi in range(w):
        if wi==0:
            dp[hi][wi] = ((dp[hi-1][wi]+dp[hi-1][wi+1])*cnt[w-2])%mod
        elif wi==w-1:
            dp[hi][wi] = ((dp[hi-1][wi]+dp[hi-1][wi-1])*cnt[w-2])%mod
        else:
            dp[hi][wi] = ((dp[hi-1][wi]+dp[hi-1][wi-1]+dp[hi-1][wi+1])*cnt[wi-2]*cnt[w-wi-2])%mod

print(dp)
print(dp[h][k-1])
