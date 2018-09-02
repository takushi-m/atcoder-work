# -*- coding: utf-8 -*-
x,y = [int(x) for x in input().split()]
ret = 1
while x<=y:
    # print(x)
    ret += 1
    x *= 2

print(ret-1)
