# -*- coding: utf-8 -*-
n = int(input())
a = []
for i,x in enumerate(input().split()):
    x = int(x)
    a.append(x-(i+1))
a = sorted(a)

if n%2==0:
    b = a[n//2-1]
else:
    b = a[n//2+1-1]

ret = 0
for x in a:
    ret += abs(x-b)
print(ret)
