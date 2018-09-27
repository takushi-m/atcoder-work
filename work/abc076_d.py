# -*- coding: utf-8 -*-
n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

T = sum(t)

def func(l,r,v,x):
    if x<=l:
        return v+(l-x)
    elif l<x<r:
        return v
    else:
        return v+(x-r)

def getv(x):
    ret = func(0,0,0,x)
    tt = 0
    for i in range(n):
        ret = min(ret, func(tt,tt+t[i],v[i],x))
        tt += t[i]
    ret = min(ret, func(tt,tt,0,x))
    return ret

ret = 0
lastv = None
for i in range(2*T):
    a1 = i*0.5
    a2 = (i+1)*0.5
    if lastv is not None:
        v1 = lastv
    else:
        v1 = getv(a1)
    v2 = getv(a2)
    lastv = v2

    ret += 0.5*0.5*(v1+v2)
print(ret)
