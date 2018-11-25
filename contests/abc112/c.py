# -*- coding: utf-8 -*-
n = int(input())
x = []
y = []
h = []
maxh = -1
for _ in range(n):
    line = list(map(int, input().split()))
    x.append(line[0])
    y.append(line[1])
    h.append(line[2])
    maxh = max(maxh, line[2])

cx = -1
cy = -1

for cx in range(0,101):
    for cy in range(0,101):
        for hi in range(maxh,maxh+120):
            flag = True
            for i in range(n):
                    hh = max(hi-abs(cx-x[i])-abs(cy-y[i]), 0)
                    if h[i]!=hh:
                        flag = False
                        break
            if flag:
                print(cx,cy,hi)
                exit()
