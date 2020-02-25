mod = 10**9+7
n,m = map(int, input().split())
fl = [int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[0] = 1
acc = [0]*(n+2)
acc[0] = 0
acc[1] = 1

s = set([fl[0]])
l = r = 0
while r<n:
    dp[r+1] = (acc[r+1]-acc[l])%mod
    acc[r+1+1] = acc[r+1]+dp[r+1]
    r += 1

    while l<n and r<n and fl[r] in s:
        s.remove(fl[l])
        l += 1
    if r<n:
        s.add(fl[r])

print(dp[n])