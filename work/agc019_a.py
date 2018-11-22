# -*- coding: utf-8 -*-
q,h,s,d = map(int,input().split())
n = int(input())

q = 4*q
h = 2*h

if n%2==0:
    t = q*n
    t = min(t, h*n)
    t = min(t, s*n)
    t = min(t, d*n//2)
else:
    t = q*n
    t = min(t, h*n)
    t = min(t, s*n)
    t = min(t, (n//2)*d + min(q,h,s))
print(t)
