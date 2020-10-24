n,k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]

mod = 998244353
d = [0]*(n+1)
dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    d[i+1] += d[i]
    d[i+1] %= mod

    dp[i] += d[i]
    dp[i] %= mod

    for l,r in lr:
        if i+l<n+1:
            d[i+l] += dp[i]
            d[i+1] %= mod
        if i+r+1<n+1:
            d[i+r+1] = (d[i+r+1]+mod-dp[i])%mod
print(dp[n-1])