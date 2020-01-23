# -*- coding: utf-8 -*-
n,d = map(int, input().split())

a2 = 0
while d%2==0:
    a2 += 1
    d //= 2
a3 = 0
while d%3==0:
    a3 += 1
    d //= 3
a5 = 0
while d%5==0:
    a5 += 1
    d //= 5

if d>1:
    print(0)
    exit()

dp = [[[[0]*(a5+1) for _ in range(a3+1)] for _ in range(a2+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
for ni in range(n):
    for i in range(a2+1):
        for j in range(a3+1):
            for k in range(a5+1):
                # 1
                dp[ni+1][min(a2,i)][min(a3,j)][min(a5,k)] += dp[ni][i][j][k]/6
                # 2
                dp[ni+1][min(a2,i+1)][min(a3,j)][min(a5,k)] += dp[ni][i][j][k]/6
                # 3
                dp[ni+1][min(a2,i)][min(a3,j+1)][min(a5,k)] += dp[ni][i][j][k]/6
                # 4
                dp[ni+1][min(a2,i+2)][min(a3,j)][min(a5,k)] += dp[ni][i][j][k]/6
                # 5
                dp[ni+1][min(a2,i)][min(a3,j)][min(a5,k+1)] += dp[ni][i][j][k]/6
                # 6
                dp[ni+1][min(a2,i+1)][min(a3,j+1)][min(a5,k)] += dp[ni][i][j][k]/6

print(dp[n][a2][a3][a5])