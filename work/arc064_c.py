# -*- coding: utf-8 -*-
line = input().split(" ")
n = int(line[0])
x = int(line[1])
a = [int(n) for n in input().split(" ")]

ret = max(0,a[0]-x)
a[0] = min(a[0],x)
for i in range(1,n):
    if a[i-1]+a[i]>x:
        r = (a[i-1]+a[i])-x
        if a[i]>=r:
            a[i] -= r
        else:
            a[i-1] -= (r-a[i])
            a[i] = 0
        ret += r

print(ret)
# print(a)
