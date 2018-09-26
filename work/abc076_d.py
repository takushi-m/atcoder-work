# -*- coding: utf-8 -*-
n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

n = 100
t = [200 for _ in range(n)]
v = [100 for _ in range(n)]

T = sum(t)

eq = [[0,0,0]]
for i in range(n):
    c = [eq[i][1],eq[i][1]+t[i],v[i]]
    eq.append(c)
eq.append([eq[n][1],eq[n][1],0])

def func(l,r,v,x):
    if x<=l:
        return v+(l-x)
    elif l<x<r:
        return v
    else:
        return v+(x-r)

def getv(x):
    ret = None
    for e in eq:
        v = func(e[0],e[1],e[2],x)
        if ret is None:
            ret = v
        else:
            ret = min(ret,v)
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
