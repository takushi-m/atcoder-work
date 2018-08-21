# -*- coding: utf-8 -*-
x = int(input())

if x<=6:
    print(1)
    exit()
if x<=11:
    print(2)
    exit()

r = x%11
ret = x//11
if r==0:
    print(2*ret)
elif r<=6:
    print(2*ret+1)
elif r<=11:
    print(2*ret+2)
