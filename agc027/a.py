# -*- coding: utf-8 -*-
n,x = map(int, input().split())
a = sorted([int(z) for z in input().split()])

ret = 0
flag = False
for i in range(n):
    if x-a[i]>=0:
        ret += 1
        x = x-a[i]
    else:
        flag = True
        break
# print(i,x,flag)
if i==n-1 and not flag and x>0:
    ret = max(0,ret-1)
print(ret)
