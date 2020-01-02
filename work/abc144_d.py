# -*- coding: utf-8 -*-
from math import tan,atan,pi
a,b,x = map(int, input().split())

def check(t):
    if t < atan(b/a):
        s = a*a*b - a*a*a*tan(t)/2
    else:
        s = a*b*b/tan(t)/2
    return x<s

ok = 0
ng = pi/2

while ng-ok>10**-8:
    mid = (ok+ng)/2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok*180/pi)