# -*- coding: utf-8 -*-
n,k = map(int, input().split())
al = list(map(int, input().split()))

def f(x):
    res = 0
    for a in al:
        res += a^x
    return res
res = 0
for x in range(k+1):
    res = max(res, f(x))
print(res)

k = bin(k)[2:]
dp = [[0, 0] for _ in range(len(k)+1)]

for d in range(len(k)):
    s1 = 0
    s0 = 0
    c = 1<<(len(k)-d-1)
    for a in al:
        if a&c>0:
            s0 += c
        else:
            s1 += c

    dp[d+1][1] = max(dp[d+1][1], dp[d][1]+max(s1,s0))
    if k[d]=="1":
        dp[d+1][1] = max(dp[d+1][1], dp[d][0]+s0)
        dp[d+1][0] = max(dp[d+1][0], dp[d][0]+s1)
    else:
        dp[d+1][0] = max(dp[d+1][0], dp[d][0]+s0)
print(dp)
print(max(dp[len(k)][0], dp[len(k)][1]))
