# -*- coding: utf-8 -*-
MOD = 10**9 + 7

def f(n):
    dp = [[0,0] for _ in range(len(n)+1)]
    dp[0][0] = 1
    for i in range(len(n)):
        for j in range(2):
            if j==1:
                x = 9
            else:
                x = int(n[i])

            for d in range(x+1):
                if j==1 or d<x:
                    dp[i+1][1] += dp[i][j]
                    dp[i+1][1] %= MOD
                else:
                    dp[i+1][0] += dp[i][j]
                    dp[i+1][0] %= MOD
    print(dp)
    return sum(dp[len(n)])

print(f("100"))
