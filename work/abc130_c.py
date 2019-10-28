# -*- coding: utf-8 -*-
w,h,x,y = map(int, input().split())

s = w*h/2

if 2*x==w and 2*y==h:
    print(s,1)
else:
    print(s,0)