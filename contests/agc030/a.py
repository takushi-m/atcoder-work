# -*- coding: utf-8 -*-
a,b,c = map(int, input().split())

if c<=a+b:
    print(b+c)
else:
    print(a+2*b+1)
