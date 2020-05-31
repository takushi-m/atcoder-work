n,s = map(int, input().split())
al = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(s+1)]
dp2 = [[set() for _ in range(n+1)] for _ in range(s+1)]

dp[0][0] = 1
for i in range(n):
    for j in range(s):
        dp[i+1][j] += dp[i][j]
        if j+al[i]<=s:
            dp[i+1][j+al[i]] += dp[i][j]
            dp2[i+1][j+al[i]] = [ss | set([i]) for ss in dp2[i][j]]

res = 0
mod = 998244353
for ss in dp2[n][s]:
    res += pow(2, n-len(ss), mod)
    res %= mod
print(res)