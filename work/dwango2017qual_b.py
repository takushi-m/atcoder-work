# -*- coding: utf-8 -*-
t = input()
n = len(t)

dp = [0 for _ in range(n+1)]

for i in range(1,n):
    tmp = 0
    if t[i-1]=="2" and t[i]=="5":
        tmp = 2
    elif t[i-1]=="2" and t[i]=="?":
        tmp = 2
    elif t[i-1]=="?" and t[i]=="5":
        tmp = 2
    elif t[i-1]=="?" and t[i]=="?":
        tmp = 2

    if tmp>0:
        dp[i] = dp[i-2] + 2

print(max(dp))
