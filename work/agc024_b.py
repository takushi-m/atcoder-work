n = int(input())
pl = [int(input()) for _ in range(n)]

d = {}
for i in range(n):
    d[pl[i]] = i

dp = [1]*n
p = 1
while p<n:
    if d[p+1]>d[p]:
        dp[d[p+1]] = dp[d[p]]+1
    p += 1
print(n-max(dp))
