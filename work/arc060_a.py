n,a = map(int, input().split())
xl = list(map(int, input().split()))

offset = 300
dp = [[0]*600 for _ in range(n+1)]
dp[0][offset] = 1
for i in range(1,n+1):
    x = xl[i-1]-a
    for j in range(-300,300):
        dp[i][offset+j] = dp[i-1][offset+j]
        if 600>offset+j-x>=0:
            dp[i][offset+j] += dp[i-1][offset+j-x]

print(dp[n][offset]-1)