# -*- coding: utf-8 -*-
n,k = map(int, input().split())
al = list(map(int, input().split()))

# def f(x):
#     res = 0
#     for a in al:
#         res += a^x
#     return res
# res = 0
# for x in range(k+1):
#     res = max(res, f(x))
# print(res)
maxd = 50
dp = [[-1, -1] for _ in range(maxd+1)]
dp[0][0] = 0

for d in range(maxd):
    s1 = 0
    s0 = 0
    c = 1<<(maxd-d-1)
    for a in al:
        if a&c>0:
            s0 += c
        else:
            s1 += c

    if dp[d][1]!=-1:
        dp[d+1][1] = max(dp[d+1][1], dp[d][1]+max(s1,s0))
    if dp[d][0]!=-1:
        if k&c>0:
            dp[d+1][1] = max(dp[d+1][1], dp[d][0]+s0)
            dp[d+1][0] = max(dp[d+1][0], dp[d][0]+s1)
        else:
            dp[d+1][0] = max(dp[d+1][0], dp[d][0]+s0)
# print(dp)
print(max(dp[maxd][0], dp[maxd][1]))
