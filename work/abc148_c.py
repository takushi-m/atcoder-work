# -*- coding: utf-8 -*-
a,b = map(int, input().split())

c = a*b

while b>0:
    a,b = b,a%b

print(c//a)