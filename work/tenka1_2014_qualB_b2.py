mod = 10**9 + 7
n = int(input())
s = input()
tl = [input() for _ in range(n)]

m = len(s)
dp = [0]*(m+1)
dp[0] = 1

for i in range(m):
    ss = s[i:]
    for t in tl:
        if ss.startswith(t):
            dp[i+len(t)] += dp[i]
            dp[i+len(t)] %= mod
print(dp[m])