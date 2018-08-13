# -*- coding: utf-8 -*-

line = input().split(" ")
d = int(line[0])
g = int(line[1])

p = []
c = []

for _ in range(d):
    line = input().split(" ")
    p.append(int(line[0]))
    c.append(int(line[1]))

dp = [[] for _ in range(d)]

for i in range(p[0]+1):
    point = 100*i
    if i==p[0]:
        point += c[0]
    dp[0].append((point, i))

for di in range(1,d):
    for dcnt in range(p[di]+1):
        dpoint = (di+1)*100*dcnt
        if dcnt==p[di]:
            dpoint += c[di]

        flag = False
        minpoint = 10000000
        mincnt = 10000000
        if dpoint>=g:
            minpoint = dpoint
            mincnt = dcnt
        print(p[di-1]+1)
        for j in range(p[di-1]+1):
            point = dp[di-1][j][0]
            cnt = dp[di-1][j][1]
            print((point,cnt))
            if point>=g:
                if cnt<mincnt:
                    minpoint = point
                    mincnt = cnt
                    flag = True
            elif point+dpoint>=g:
                if cnt+dcnt<mincnt:
                    minpoint = point+dpoint
                    mincnt = cnt+dcnt
                    flag = True
        if not flag:
            minpoint = dpoint
            mincnt = dcnt
        dp[di].append((dpoint, dcnt))
        dp[di].append((minpoint, mincnt))
    print("---")
    print(dp[di])

for dpc in dp[-1]:
    if dpc[0]>=g:
        print(dpc)
