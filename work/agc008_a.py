# -*- coding: utf-8 -*-
x,y = map(int, input().split())

if x==0:
    res = abs(y)
    if y<0:
        res += 1
    print(res)
    exit()
if y==0:
    res = abs(x)
    if x>0:
        res += 1
    print(res)
    exit()

if x*y<0:
    print(1+abs(abs(y)-abs(x)))
elif x<y:
    print(y-x)
else:
    print(2+x-y)
