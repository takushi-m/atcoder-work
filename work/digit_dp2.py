# -*- coding: utf-8 -*-
MOD = 10**9 + 7

def f(n):
    nlen = len(n)
    dp = [[[0,0], [0,0]] for _ in range(nlen+1)]
    dp[0][0][0] = 1
    for i in range(nlen):
        for j in range(2):
            for k in range(2):
                if j==1:
                    x = 9
                else:
                    x = int(n[i])
                for d in range(x+1):
                    if j==1 or d<x:
                        jj = 1
                    else:
                        jj = 0

                    if k==1 or d==3:
                        kk = 1
                    else:
                        kk = 0

                    dp[i+1][jj][kk] += dp[i][j][k]
                    dp[i+1][jj][kk] %= MOD
    return dp[nlen][0][1]+dp[nlen][1][1]

print(f("10"))
