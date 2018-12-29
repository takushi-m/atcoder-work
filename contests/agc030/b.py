# -*- coding: utf-8 -*-
l,n = map(int, input().split())
xl = [int(input()) for _ in range(n)]
xl.sort()

dp = [[(0,-1,0), (0,n,0)] for _ in range(n+1)]

for i in range(n):
    s0,i0,c0 = dp[i][0]
    s1,i1,c1 = dp[i][1]

    if s0+(xl[i0+1]-c0+l)%l > s1+(xl[i0+1]-c1+l)%l:
        dp[i+1][0] = (
            s0+(xl[i0+1]-c0+l)%l,
            i0+1,
            xl[i0+1]
        )
    else:
        dp[i+1][0] = (
            s1+(xl[i0+1]-c1+l)%l,
            i0+1,
            xl[i0+1]
        )

    if s0+(c0-xl[i1-1]+l)%l > s1+(c1-xl[i1-1]+l)%l:
        dp[i+1][1] = (
            s0+(c0-xl[i1-1]+l)%l,
            i1-1,
            xl[i1-1]
        )
    else:
        dp[i+1][1] = (
            s1+(c1-xl[i1-1]+l)%l,
            i1-1,
            xl[i1-1]
        )
print(dp)
print(max(dp[n][0][0],dp[n][1][0]))


#
# visited = [False]*n
#
# s = 0
# res = 0
# left = 0
# right = 0
# while not all(visited):
#     s1 = -1
#     s2 = -1
#     i1 = -1
#     i2 = -1
#     for i in range(n):
#         if not visited[i] and s1<0:
#             s1 = (xl[i] - s + l)%l
#             i1 = i
#         if not visited[n-i-1] and s2<0:
#             s2 = (s - xl[n-i-1] + l)%l
#             i2 = n-i-1
#         if s1>0 and s2>0:
#             break
#
#     # if s1>s2:
#     if (s2-right+l)%l < (left-s1+l)%l:
#         res += s1
#         visited[i1] = True
#         s = xl[i1]
#         right = s
#         print(i1,s1,res,s)
#     else:
#         res += s2
#         visited[i2] = True
#         s = xl[i2]
#         left = s
#         print(i2,s2,res,s)
#
# print(res)
