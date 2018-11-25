# -*- coding: utf-8 -*-
line = input().split(" ")
N = int(line[0])
M = int(line[1])
Q = int(line[2])

memo = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    line = input().split(" ")
    l = int(line[0])
    r = int(line[1])
    memo[l][r] += 1

for _ in range(Q):
    line = input().split(" ")
    p = int(line[0])
    q = int(line[1])

    ret = 0
    for i in range(p,q+1):
        for j in range(i,q+1):
            ret += memo[i][j]
    print(ret)
