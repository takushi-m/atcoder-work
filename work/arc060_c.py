# -*- coding: utf-8 -*-
line = input().split(" ")
n = int(line[0])
a = int(line[1])
x = [int(i) for i in input().split(" ")]

X = max(max(x), a)

dp = [[[0 for s in range(n*a+1)] for k in range(n+1)] for j in range(n+1)]

dp[0][0][0] = 1
ret = 0
for j in range(n+1):
    for k in range(n+1):
        for s in range(n*a+1):
            if j>0 and s<x[j-1]:
                dp[j][k][s] = dp[j-1][k][s]
            elif j>0 and k>0 and s>=x[j-1]:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j-1]]

ret = 0
for k in range(1,n+1):
    ret += dp[n][k][k*a]
print(ret)
