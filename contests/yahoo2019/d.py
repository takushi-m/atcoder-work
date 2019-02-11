# -*- coding: utf-8 -*-
l = int(input())
al = [int(input()) for _ in range(l)]
INF = 10**15
dp = [INF]*5  # 0,偶数,奇数,偶数,0の状態
dp[0] = 0

def cost(i, k):
    # i番目を状態kにした時に必要な回数
    if k==0 or k==4:
        return al[i]
    elif k==1 or k==3:
        if al[i]>0:
            return al[i]%2
        else:
            return 2
    else:
        if al[i]%2==0:
            return 1
        else:
            return 0

for i in range(l):
    dp2 = [min(dp[:j+1]) for j in range(5)]
    for j in range(5):
        dp[j] = dp2[j] + cost(i,j)

    # for j in range(5):
    #     for k in range(j,5):
    #         dp[i+1][k] = min(
    #             dp[i+1][k],
    #             dp[i][j] + cost(i, k)
    #         )

print(min(dp))
