# -*- coding: utf-8 -*-
n = int(input())
aa = [0]
s = 0
for x in input().split():
    a = int(x)
    aa.append(aa[-1]+a)
    s += a

ret = abs(2*aa[1]-s)
for i in range(1,n):
    if abs(aa[i]-(s-aa[i]))<ret:
        ret = abs(aa[i]-(s-aa[i]))

print(ret)
