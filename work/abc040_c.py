n = int(input())
al = list(map(int, input().split()))
dp = [10**9]*n
dp[0] = 0
dp[1] = abs(al[0]-al[1])

for i in range(2,n):
    dp[i] = min(dp[i-1]+abs(al[i]-al[i-1]), dp[i-2]+abs(al[i]-al[i-2]))
# print(dp)
print(dp[n-1])
