n,k = map(int, input().split())

dp = [1]*k

for _ in range(n-1):
    s = sum(dp)
    for i in range(k):
        dp[i] = s - dp[i]
print(sum(dp))