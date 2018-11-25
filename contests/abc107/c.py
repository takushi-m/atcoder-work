# -*- coding: utf-8 -*-
line = input().split()
n = int(line[0])
k = int(line[1])
x = [int(i) for i in input().split()]


ret = 9**10
for i in range(n-k+1):
    mins = x[i]
    maxs = x[i+k-1]
    if mins<0 and maxs>0:
        if abs(mins)<maxs:
            r = abs(mins)*2+maxs
        else:
            r = maxs*2+abs(mins)
    elif maxs<=0:
        r = abs(mins)
    else:
        r = maxs

    if r<ret:
        ret = r

print(ret)
