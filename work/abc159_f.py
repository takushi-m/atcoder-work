mod = 998244353
n,s = map(int, input().split())
al = list(map(int, input().split()))

dp = [[0]*(s+1) for _ in range(n+1)]
res = 0
for i in range(n):
    a = al[i]
    dp[i+1][0] += 1
    dp[i+1][0] %= mod
    if a<=s:
        dp[i+1][a] += 1
        dp[i+1][a] %= mod
    for j in range(s+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        if j+a<=s:
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a] %= mod
    res += dp[i+1][s]
    res %= mod
print(res)